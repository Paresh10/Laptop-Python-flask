from flask import Flask

# Set Debug =  true and port =  8000
DEBUG= True
PORT=8000

# Set app = flask
app =   Flask(__name__)




if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
