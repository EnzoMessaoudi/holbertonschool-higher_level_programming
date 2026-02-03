#!/usr/bin/python3


"""
Modulo that write a class BaseGeometry
"""


class BaseGeometry:
    """
    Class that define a geometry
    """
    def area(self):
        """
        For the moment, raise an error if the user want to access
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates 'value'
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class that create a rectangle
    """
    def __init__(self, width, height):
        """
        Create Two attribute for a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
