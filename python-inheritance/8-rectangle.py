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
        Public instance method that validates 'value'
        Assumes 'name' is always a string
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height
