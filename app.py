from flask import Flask, jsonify

# Import Cors here
from flask_cors import CORS

# Import laptops file here
from resources.laptops import laptops

# Import models here
import models

# Set Debug =  true and port =  8000
DEBUG= True
PORT=8000

# Set app = flask
app =   Flask(__name__)


#Implement CORS here
# First Arg = Blueprint
# Second Arg = Origin to be allowed
# Third Arg = To enable cookies for in order to use it as session
CORS(laptops, origins=['http://localhost:3000'], supports_credentials=True)


# Setup the blueprint to use here
app.register_blueprint(laptops, url_prefix='/api/v1/laptops')

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
