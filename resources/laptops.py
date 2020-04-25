import models

# Import Blueprint from flask
# request & jsonify -  Get the data from client in json
from flask import Blueprint, request, jsonify

# Important peewee tool
from playhouse.shortcuts import model_to_dict


# Create a Blueprint here
laptops = Blueprint('laptops', 'laptops')
