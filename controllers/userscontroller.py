from flask import request, redirect, render_template, url_for, flash, make_response
from views.register import RegistrationForm
from views.login import LoginForm
from dto.requestdto import post_request, get_request
from root import application, bcrypt
from json import loads, dumps
from helpers import *
from decorators import *

@application.route("/user", methods=["GET", "POST"])
def user():
    user_token = request.cookies.get(application.config["UID_HEADER"])
    headers = loads(decode(user_token))
    if headers != None:
        user_object = {
            "username": headers["username"]
        }
        user = get_request("users/username", user_object, headers)
        status = loads(user["response"])["status"]
        if status == "success":
            responseObject = make_response(render_template("user.html", response=headers, current_user=headers["username"]))
            return responseObject
        else:
            message = loads(user["response"])["message"]
            flash(message, "error")
            return redirect(url_for("signin"))
    else:
        return redirect(url_for("signin"))

@application.route("/signin", methods=["GET", "POST"])
@user_token_validity_check
def signin(*args, **kwargs):
    form = LoginForm()    
    if request.method == 'GET':        
        return render_template('signin.html', form=form, current_user=kwargs['current_user'])
    if request.method == 'POST':
        if form.validate_on_submit():
            params = {
                "email": form.email.data,
                "password": form.password.data
            }
            headers = {}
            responseObject = loads(post_request("auth/login", params, headers)["response"])
            if responseObject["status"] == "success":
                redirectObject = redirect(url_for("user"), code=307)
                cookie = {
                    "token": responseObject["auth_token"],
                    "username": responseObject["username"]
                }
                redirectObject.set_cookie(application.config["UID_HEADER"], encode(dumps(cookie)))
                return redirectObject
            else:
                flash(responseObject['message'], 'error')
                return render_template('signin.html', form=form, current_user=kwargs['current_user'])
        return render_template('signin.html', form=form, current_user=kwargs['current_user'])
        

@application.route("/signup", methods=["GET", "POST"])
@user_token_validity_check
def signup(*args, **kwargs):
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        data = {
            "username": form.username.data,
            "email": form.email.data,
            "password": hashed_password
        }
        headers = {}
        result = loads(post_request("users", data, headers)['response'])
        flash(result['user']['username'], "success")
        return redirect(url_for("index"))
    return render_template('signup.html', form=form, current_user=kwargs['current_user'])

@application.route("/signout")
@user_token_validity_check
def signout(*args, **kwargs):
    responseObject = make_response(render_template("index.html", current_user=None))
    responseObject.delete_cookie(application.config["UID_HEADER"])
    return responseObject

@application.route("/profile")
@user_token_validity_check
def profile(*args, **kwargs):
    return render_template('profile.html', current_user=kwargs['current_user'])