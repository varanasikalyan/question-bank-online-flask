#-------------------------------------------------------------------------------
# Name:        Login Form Module
# Purpose:
#
# Author:      kkrishnav
#
# Created:     17/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign In")