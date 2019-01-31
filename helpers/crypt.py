import base64
from root import application

def encode(decoded):
    return base64.urlsafe_b64encode(bytes(decoded, "utf-8"))

def decode(encoded):
    return base64.urlsafe_b64decode(encoded)