In this project, we will see about the OOP, the Object oriented Programming

What is OOP
    OPP means Object oriented Programming. It's a programing method where we organize our program inside what's called an object, where we combine data and functionality.
“first-class everything”
    It'a a term designed by Guido van Rossum. He assumes that in OOP of Python, everything need to be first class, it means that everything have the same status, it's all treated the same way.
What is a class
    A class provide a means of bundling data and functionality together. Those are instance of the class created. Classes has two part: the header (class name()) and the body part, wich consist of an indented block of statements.
What is an object and an instance
    Object and instance is what are used to store data inside of a class.
What is the difference between a class and an object or instance
    A class is where objects and instances are stocked. Meanwhile, object and instance are where the datas are stored.
What is an attribute
    Specification that defines a property of an object or element. It's the identity of a element.
What are and how to use public, protected and private attributes
What is self

What is a method
    A method is a function binded to a class attribute

What is the special __init__ method and how to use it
    __init__ is used to pick up the data that the user gived us by putting it at the begginig of our class, It's used to initialized an instance.

What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
How to dynamically create arbitrary new attributes for existing instances of a class

How to bind attributes to object and classes
    We can bind attributes to object and classes by creating an object and saying that this object is equal to our attributes

What is the __dict__ of a class and/or instance of a class and what does it contain
    __dict__ is the way to see what's inisde of the dictionnary of a class or an object.

How does Python find the attributes of an object or class
    The attributes of object or class are stocked in a dictionnary. We can see it by using __dict__ to see what's iniside.

How to use the getattr function
    The getattr function is used to prevent exceptions by searching an attribute that don't exist. You just have to provide a default value as the the third argument ->getattr(x, 'energy', 100) (energy = attribute name)