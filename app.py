from flask import Flask, jsonify

# Set Debug =  true and port =  8000
DEBUG= True
PORT=8000

# Set app = flask
app =   Flask(__name__)


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
    app.run(debug=DEBUG, port=PORT)
