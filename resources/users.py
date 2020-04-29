import models

#Import a blueprint here
from flask import Blueprint, request, jsonify

#Import password related dependencies here
from flask_bcrypt import generate_password_hash, check_password_hash

#Import model_to_dict here from peewee - playhouse
from playhouse.shortcuts import model_to_dict

#import log_in from flask
# login user is important and used for
# session to keep track of user
from flask_login import login_user

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


#Login route for user
@users.route('/login', methods=['GET'])
def log_in():

    payload = request.get_json()
    #Check users email for logging them in
    try:
        user = models.User.get(models.User.email == payload['email'])

        user_dict = model_to_dict(user)

        #If user exist than check thir password
        correct_password = check_password_hash(
            user_dict['password'],
            payload['password']
            )
        #If password right then log in the user
        if(correct_password):
            login_user(user)

        # Respond with data and remove the password
        user_dict.pop('password')

        return jsonify(
            data=user_dict,
            message=f"Logged in as {user_dict['email']}",
            status=200
        ), 200

        #If password not right respond incorrect password

        #else if user does not exist

        # respond username or password not correct




    except models.DoesNotExist:
        print('Username not good')

        return jsonify(
            data={},
            message="Email or password incorrect",
            status=401
        ), 401






    #
