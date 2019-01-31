from flask import request, render_template, flash
from root import application
from json import loads, dumps
from dto.requestdto import post_request
from helpers import *
from decorators import *
from itertools import repeat

@application.route("/question", methods=["POST", "GET"])
@user_token_validity_check
def question(*args, **kwargs):
	if request.method == "GET":
		if kwargs['current_user'] == None:
			return render_template('index.html', current_user=kwargs['current_user'])
		else:
			return render_template('question.html', current_user=kwargs['current_user'])
	if request.method == 'POST':
		question_text = request.form['question']
		selected_type = request.form['selectedType']
		
		if selected_type == "multiple":
			number_of_options = int(request.form['optionsQty'])
			# list comprehension
			options = list(map(build_option, range(number_of_options), repeat(request.form)))
			question = {
				"question": question_text,
				"options": options
			}        
		user_token = request.cookies.get(application.config["UID_HEADER"])
		headers = loads(decode(user_token))
		responseObject = loads(post_request("questions", question, headers)["response"])
		if responseObject["status"] == "success":
			flash(responseObject['message'], 'info')
		else:
			flash(responseObject['message'], 'error')            
	return render_template('question.html', current_user=kwargs['current_user'])

def build_option(i, form):
	correction = 1 if 'option' + str(i + 1) in form else 0
	option = {
		"option": form['option' + str( i + 1 ) + 'Text'],
		"is_correct_option": correction
	}
	return option