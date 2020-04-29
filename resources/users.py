import models

#Import a blueprint here
from flask import Blueprint, request, jsonify

#Import password related dependencies here
from flask_bcrypt import generate_password_hash

# Convert it to a blueprint
users = Blueprint('users', 'users')

#Get route for users
@users.route('/', methods=['GET'])
def get_all_users():
    return 'Here are the users'



# Users Signup route
@users.route('/signup', methods=['POST'])
def sign_up():

    payload = request.get_json()

    #LowerCase username and email using payload
    payload['username'] = payload['username'].lower()
    payload['email'] = payload['email'].lower()

    print(payload)

    try:
        models.User.get(models.User.email == payload['email'])

        return jsonify(
            date={},
            message="Username with this email already exist",
            status=401
        ), 401


    except models.DoesNotExist:

        #hash the password with bcrypt
        password_hash = generate_password_hash(payload['password'])

        #Create a user here
        user_created=models.User.create(
            username=payload['username'],
            email=payload['email'],
            password=password_hash
        )

        print(user_created)

        return 'Hey'











    #
