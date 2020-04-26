import models

# Import Blueprint from flask
# request & jsonify -  Get the data from client in json
from flask import Blueprint, request, jsonify

# Important peewee tool
from playhouse.shortcuts import model_to_dict


# Create a Blueprint here
laptops = Blueprint('laptops', 'laptops')


# Get route for laptops
@laptops.route('/', methods=['GET'])
def laptops_model():
    laptops = models.Laptop.select().dicts()

    return jsonify(
        data=[laptop for laptop in laptops],
        message="Found {} laptops in the database".format(len(laptops)),
        status = 201
        ), 201


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

    print(new_laptop.__dict__)

    laptop_dict = model_to_dict(new_laptop)

    return jsonify(
        data=laptop_dict,
        message="{} laptop was created".format(laptop_dict['model']),
        status=201
    ), 201






    # return "Here is "
