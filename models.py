from peewee import *

# import python built in date here
import datetime
# Databse
DATABASE = SqliteDatabase('laptops.sqlite')

# Create a model here
class Laptop(Model):

    # Special contructor which gives intstruction
    # to the model on coonection and storage
    class Meta:
        database = DATABASE

    maker = CharField() # String
    model = CharField() # String
    manufactured_on: DateField(default=datetime.datetime.date)

def connectToLaptopDatabase():
    DATABASE.connect()

    DATABASE.create_tables([Laptop], safe=True)
    print("Now connected with Laptop-Database and created table if there were none")

    # Close the connectio here
    DATABASE.close()
