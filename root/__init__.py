#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      kkrishnav
#
# Created:     15/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__, static_url_path='/static')
application.config.from_pyfile("configs.cfg")

bcrypt = Bcrypt(application)
login_manager = LoginManager(application)

from controllers import *