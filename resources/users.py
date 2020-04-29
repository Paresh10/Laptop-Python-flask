import models

#Import a blueprint here
from flask import Blueprint, request, jsonify

#Import password related dependencies here
from flask_bcrypt import generate_password_hash

#Import model_to_dict here from peewee - playhouse
from playhouse.shortcuts import model_to_dict

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

        #Convert user_created in to the dictionary
        user_created_dict = model_to_dict(user_created)
        print(user_created_dict)

        #Password can not be jsonf. The password type is byte
        print(type(user_created_dict['password']))

        #Pop the password out when sending user data
        user_created_dict.pop('password')

        return jsonify(
            data=user_created_dict,
            message=f"Congrats you can log in using {user_created_dict['email']}",
            status=201
        ), 201











    #
