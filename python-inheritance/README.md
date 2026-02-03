- What is a superclass, baseclass or parentclass
    This class is the base of our module. This is the first class we created and can be heritited to other subclasses.
- What is a subclass
    A subclass is a class that heritate from an other superclass, which will be her mother.
- How to list all attributes and methods of a class or instance
    We can use vars() function. This take a class as a paramater and will display the attributes of a class.
- When can an instance have new attributes
    Using __init__ and self. The attributes of an instance can be created this way and the other class will all have unique attribute.
- How to inherit class from another
    class test(object)
- How to define a class with multiple base classes
    class test2(object, test)
- What is the default class every class inherit from
    A class which name is Object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only), but it does allow Python to treat all objects in the same way.
- How to override a method or attribute inherited from the base class
    super.__init__(name, age). It will pick the attributes of the mother class and override the attributes of the actual class.
- Which attributes or methods are available by heritage to subclasses
    Any attributes and methods can be pick up as long as they are not private.
- What is the purpose of inheritance
    It is use for better codding and organisation, use attributes again and create a hierarchy inside of a baseclass.
- What are, when and how to use isinstance, issubclass, type and super built-in functions
    .isinstance is used to check the instance of a class. Return true if it's the good type or false if not.
    .issubclass check if a class belong to this mother class. Same return as isinstance.
    .super() is used to search back inside the mother class the attributes and datas.