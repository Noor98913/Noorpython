On the fourth day, we learned about the below concepts that will make us able to write more helpful and complex projects, also we took examples for each one.

-Class Methods and Static Methods
In Python, we can define class methods and static methods using the @classmethod and @staticmethod decorators respectively.
-Class attributes:
    • Class attributes are attributes that are set at the class-level, as opposed to the instance-level.
    Note: Class attributes are shared among all instances of the class, while object/instance attributes are specific to each instance.
class <class_name>:
    <class_attribute> = <value>
    def __init__(self):
        self.<object_attribute> = <value>


-Class methods:
    • Class methods are methods that are bound to the class and not the object
    • They have access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    • They can modify the class state that would apply across all instances of the class.
    • A class method takes cls as the first implied argument.
    • You can define a class method using the @classmethod decorator.
class <class_name>:
    @classmethod
    def <method_name>(cls, <parameters>):
        pass

-Static methods:
    • Static methods are methods that are bound to the class and not the object of the class.
    • They do not modify the state of the class or the instance.
    • They are used when a method does not access the instance or class state.
    • You can define a static method using the @staticmethod decorator.
class <class_name>:
    @staticmethod
    def <method_name>(<parameters>):
        pass



-Encapsulation
Encapsulation is the concept of restricting access to certain parts of an object. In Python, we can restrict access to certain parts of an object by using private or protected attributes and methods.


-Property Decorators
In Python, we can define properties using the @property decorator. Properties allow us to define a method that can be accessed as an attribute. This is useful when we want to define an interface for accessing a protected or a private attribute.




-Abstract Classes and Methods
Abstract classes are classes that cannot be instantiated and are meant to serve as blueprints for other classes. Abstract methods are methods declared in an abstract class but have no implementation in the abstract class itself. Subclasses of the abstract class are required to provide concrete implementations for these abstract methods.
    Absraction is a way to hide the implementation details and show only the functionality to the user.




-Multiple Inheritance
Multiple Inheritance is a concept in Object-Oriented Programming (OOP) where a class can inherit attributes and methods from more than one superclass. In Python, you can create a class that inherits from multiple superclasses, and Python uses a method resolution order (MRO) to determine the order in which methods are called when there are conflicts between inherited methods.




-Method Chainning
Method Chaining is a technique that allows you to call multiple methods on an object consecutively in a single line of code. It's achieved by having each method return the object itself (self), enabling the chaining of method calls.


