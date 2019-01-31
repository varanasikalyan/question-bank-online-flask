#-------------------------------------------------------------------------------
# Name:        Application requests
# Purpose:
#
# Author:      kkrishnav
#
# Created:     19/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from requests import post, get, delete
from root import application
from json import dumps

def post_request(entity, post_data, headers):
    uri = application.config["API_URL"].format(entity)
    request_headers = dict(application.config["API_HEADERS"])
    request_headers.update(headers)
    responseObj = post(url=uri, data=dumps(post_data), headers=request_headers)
    return {
        "response":responseObj.text
    }

def get_request(entity, get_data, headers):
    uri = application.config["API_URL"].format(entity)
    request_headers = dict(application.config["API_HEADERS"])
    request_headers.update(headers)
    responseObj = get(url=uri, params=get_data, headers=request_headers)
    return {
        "response":responseObj.text
    }