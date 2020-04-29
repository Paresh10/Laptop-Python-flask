from flask import Flask, jsonify

# Import models here
import models

# Import Cors here
from flask_cors import CORS

#Import LoginManager here from flask
from flask_login import LoginManager

# Import laptops blueprints here
from resources.laptops import laptops

#import users blueprints here
from resources.users import users


# Set Debug =  true and port =  8000
DEBUG= True
PORT=8000

# Set app = flask
app =   Flask(__name__)

#Setup a secret key for session
app.secret_key = "Flask with React is powerful!"

#Instantiate a login manager
login_manager = LoginManager()

#Connecting app with login LoginManager
login_manager.init_app(app)

#Implement CORS here
# First Arg = Blueprint
# Second Arg = Origin to be allowed
# Third Arg = To enable cookies for in order to use it as session
CORS(laptops, origins=['http://localhost:3000'], supports_credentials=True)

#Implement CORS route for users here
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)


# Setup the blueprint to use here
app.register_blueprint(laptops, url_prefix='/api/v1/laptops')

## Setup the blueprint for users
app.register_blueprint(users, url_prefix='/api/v1/users')

# Get home route
@app.route('/')
def greetings():
    return "Hello world!"

@app.route('/pets')
def my_pets():
    cat = [
        {
            'name': 'Sanjay',
            'age': 4,
            'color': 'orange'
    },
        {
            'name': 'Cathy',
            "age": 2,
            'color': 'buff'
        }
    ]
    dog = {
        'name': 'Buddy',
        'age': 2,
        'color': 'baige'
    }

    return jsonify(name="Paresh", pets=[cat, dog])






# Set up a PORT here
if __name__ == '__main__':

    # Require database here
    models.connectToLaptopDatabase()
    app.run(debug=DEBUG, port=PORT)
