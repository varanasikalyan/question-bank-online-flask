from flask import redirect, render_template
from root import application
from decorators import *

@application.route("/")
@user_token_validity_check
def index(*args, **kwargs):
	return render_template('index.html', current_user=kwargs['current_user'])

@application.route("/about")
@user_token_validity_check
def about(*args, **kwargs):
	return render_template('about.html', current_user=kwargs['current_user'])

@application.route("/careers")
@user_token_validity_check
def careers(*args, **kwargs):
	return render_template('careers.html', current_user=kwargs['current_user'])

@application.route("/contact")
@user_token_validity_check
def contact(*args, **kwargs):
	return render_template('contact.html', current_user=kwargs['current_user'])

@application.route("/bootstrap")
@user_token_validity_check
def bootstrap(*args, **kwargs):
	return render_template('bootstrap.html', current_user=kwargs['current_user'])