class Animal:
    """Animal class"""
    def __init___(self, name):
        print("Initializing name")
        self._name = name

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Setting name")
        self._name = new_name

    @property
    def species(self):
        print("Getting species")
        return self.species

    @name.setter
    def species(self, new_species):
        print("Setting species")
        self._name = new_species

    def __init__(self, age):
        print("Initializing Age")
        self._age = age

    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Book:
    """Book Class"""

def __init__(self, name):
    print("Initializing Name")
    self._name = name

@property
def name(self):
    print("Getting Name")
    return self._name

@name.setter
def name(self, new_name):
    print("Setting Name")
    self._name = new_name

def __init__(self, author):
    print("Initializing Author")
    self._author = author

@property
def author(self):
    print("Getting author")
    return self.author

@name.setter
def name(self, new_author):
    print("Setting Author")
    self._name = author

def __init__(self, yearPublished):
    print("yearPublished")
    self._yearPublished = yearPublished

@property
def yearPublished(self):
    print(yearPublished)
    return self._yearPublished

def __init__(self, ISBN):
    print("ISBN")
    self._ISBN = ISBN

@property
def ISBN(self):
    print("ISBN")
    return self._ISBN

def read(self):
    print("Reading")

class Vehicle:
    """Vehicle Class"""

def __init__(self, make):
    print("Initializing Make")
    self._make = make

@property
def make(self):
    print("Make of the vehicle")
    return self._make

def __init__(self, model):
    print("Initializing Model")
    self.model = model

@property
def model(self):
    print("Model of the vehicle")
    return self.model

def __init__(self, color):
    print("Initializing Color")
    self.color = color

@property
def color(self):
    print("Color of the vehicle")
    return self.color

def __init__(self, VIN):
    print("Initializing VIN")
    self.VIN = VIN

def run(self):
    print("Vehcile running")

def brake(self):
    print("Vehicle Braking")





        


    
