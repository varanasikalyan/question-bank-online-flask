from flask import request, Response
from json import loads
from root import application
from functools import wraps
from jwt import decode
from dto.requestdto import get_request
from helpers import *

def user_token_validity_check(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user_token = request.cookies.get(application.config["UID_HEADER"])
        kwargs['current_user'] = None
        if user_token != None:
            user_token = loads(decode(user_token))                   
            if "token" in user_token and "username" in user_token:        
                try:
                    params = {}                    
                    responseObject = loads(get_request("token/validate", params, user_token)["response"])
                    if responseObject["status"] == "success":
                        kwargs['current_user'] = user_token["username"]
                                    
                    return f(*args, **kwargs)
                except:             
                    return f(*args, **kwargs)
            else:           
                return f(*args, **kwargs)
        else:
            return f(*args, **kwargs)
    return wrapper