import models

# Import Blueprint from flask
# request & jsonify -  Get the data from client in json
from flask import Blueprint, request, jsonify

# Important peewee tool
from playhouse.shortcuts import model_to_dict


# Create a Blueprint here
laptops = Blueprint('laptops', 'laptops')


# Get route for laptops
# @laptops.route('/', methods=['GET'])
# def laptops_model():
#     laptops = models.Laptop.select()
#     print('All the detai; of the laptops')
#     print(laptops)

# Create laptops route
@laptops.route('/', methods=['POST'])
def create_laptop():
    """This function creates a laptop in the database"""

    payload = request.get_json() # similar to req.body

    # create a laptop here
    new_laptop = models.Laptop.create(
        maker=payload['maker'],
        model=payload['model'],
        manufactured_on=payload['manufactured_on'])

    print(new_laptop)
    print(new_laptop.__dict__)
    return "Here is "
