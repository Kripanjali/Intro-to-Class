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

class Fish(Animal):
    """Fish class, inheriting from Animal"""

    def __init__(self, colorName,id):
        print("Initializing name")
        super().__init__(colorName)
        self.__colorid = id

    @property
    def color(self):
        print("Getting Name")
        return self.__colorid

    @color.setter
    def colorName(self, new_id):
        print("Setting Name")
        self.__colorid = new_id

class Snake(Animal):
    """Snake class, inheriting from Animal"""

    def __init__(self,groupName,id):
        print("Initializing name")
        super().__init__(groupName)
        self.__groupid = id

    @property
    def group(self):
        print("Getting Name")
        return self.__groupid

    @group.setter
    def groupName(self, new_id):
        print("Setting Name")
        self.__groupid = new_id

class Person(Animal):
    """Person class, inhertiting from Animal"""

    def __init__(self,personName,id):
        print("Initializing name")
        super().__init__(personName)
        self.__personid = id

    @property
    def person(self):
        print("Getting Name")
        return self.__personid

    @person.setter
    def personName(self, new_id):
        print("Setting Name")
        self.__personid = new_id

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
    self._name = new_author

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
    return self.read

class Textbook(Book):
    """Textbook class, inheriting from Book"""
    def __init__(self,objective,id):
        print("Initializing objective")
        super().__init__(objective)
        self.__tbID = id

@property
def textbookID(self):
    print("Getting objective")
    return self.__tbID

@textbookID.setter
def objective(self, new_id):
    print("Setting objective")
    self.__tbID = new_id

class AddressBook(Book):
    """Address Book class inheriting from Book"""
    def __init__(self,zipcode,id):
        print("Initializing Address Book")
        super().__init__(zipcode)
        self.__addid = id

@property
def addressbookID(self):
    print("Getting Address Book")
    return self.__addid

@addressbookID.setter
def zipcode(self, new_id):
    print("Setting Zipcode")
    self.__addid = new_id
