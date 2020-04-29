import models

#Import a blueprint here
from flask import Blueprint

# Convert it to a blueprint
users = Blueprint('users', 'users')

#Get route for users
@users.route('/', methods=['GET'])
def get_all_users():
    return 'Here are the users'
