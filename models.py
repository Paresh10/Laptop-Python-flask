from peewee import *

# import python built in date here
from datetime import date

# Import flask and UserMixin here
from flask_login import UserMixin


# Databse
DATABASE = SqliteDatabase('laptops.sqlite')

# Create User model here
class User(UserMixin, Model):
    # Special contructor which gives intstruction
    # to the model on conection and storage
    class Meta:
        database = DATABASE

    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()


# Create a model here
class Laptop(Model):

    # Special contructor which gives intstruction
    # to the model on conection and storage
    class Meta:
        database = DATABASE

    maker = CharField() # String
    model = CharField() # String
    manufactured_on = DateField()

def connectToLaptopDatabase():
    DATABASE.connect()

    DATABASE.create_tables([User, Laptop], safe=True)
    print("Now connected with Laptop-Database and created table if there were none")

    # Close the connectio here
    DATABASE.close()
