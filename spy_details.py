# This file contains the default spy data which would be imported in the main.py

#This class defines the specifications of a spy
class spy:
    def __init__(self, name, salutation, age, rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating

#Declaring the default spy
default_spy=spy('Bond','Mr',32,4.8)
