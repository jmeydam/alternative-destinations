from flask import current_app
from flask_httpauth import HTTPBasicAuth
from . import api
from .errors import unauthorized

auth = HTTPBasicAuth()

@auth.verify_password
def verfiy_password(username, password):
    #print("verify_password('" + username + "', '" + password + "')")
    #print("if 'user_01' password must match '" + current_app.config['PASSWORD_USER_01'] + "'")
    if username == '' or password == '':
        return False
    elif username == 'user_01' and password == current_app.config['PASSWORD_USER_01']:
        return True
    elif username == 'user_02' and password == current_app.config['PASSWORD_USER_02']:
        return True
    else:
        return False

@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')
