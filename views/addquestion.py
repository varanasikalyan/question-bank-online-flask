#-------------------------------------------------------------------------------
# Name:        Add Question Form Module
# Purpose:
#
# Author:      kkrishnav
#
# Created:     17/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dto.requestdto import get_request
from json import loads

class AddQuestionForm(FlaskForm):
    username = StringField("Username",
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                    validators=[DataRequired(),
                                    EqualTo("password")])
    submit = SubmitField("Sign Up")