On the third day, we learned the basic concepts of Object-Oriented Programming (OOP) 


Classes and Objects


Class: is a blueprint or template for creating objects, attributes (data) and methods (functions) that the objects of the class will have.

Objects: an instance of a class.

Objects:

<variable_name> = <class_name>()


# Create objects (instances) of the class
dog1 = Dog("Buddy", "Golden Retriever", "Hello")
print(dog1.bark())
dog2 = Dog("Daisy", "Labrador")


Attributes and Methods

methods = functions

Attributes:

Attributes are variables that store data for an object

class <class_name>:
    <class_attribute> = <value>
    def __init__(self):
        self.<object_attribute> = <value>


Constructor Method:


class <class_name>:
    def __init__(self, <parameter>):
        self.<attribute> = <parameter>


Inheritance

Inheritance allows you to create a new class (subclass or child class) that inherits properties and methods from an existing class (superclass or parent class). It promotes code reusability.
Creating a Subclass
To create a subclass, pass the parent class as a parameter to the subclass. The subclass inherits all the attributes and methods of the parent class.
class <subclass_name>(<parent_class_name>):
    pass


Method Overriding
Method overriding allows a subclass to provide a specific implementation of a method that is already provided by its parent class. This is useful when you want to change the behavior of a method in the subclass.
class <superclass_name>:
    def my_method(self):
        print("Hello from the superclass")
class <subclass_name>(<superclass_name>):
    def my_method(self):
        print("Hello from the subclass")


Overriding default methods
Python provides several default methods that you can override in your classes. These methods are called magic methods or dunder methods because they are enclosed in double underscores.
__str__ Method
The __str__ method returns a string representation of the object. You can override this method to return a custom string representation.
class <class_name>:
    def __str__(self):
        return "<custom_string>"
__add__ Method
The __add__ method allows you to define the behavior of the + operator for objects of the class.
class <class_name>:
    def __add__(self, other):
        return self.<attribute> + other.<attribute>
similarly, you can override other default methods like __eq__, __lt__, __gt__, __len__, etc.



















