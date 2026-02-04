#!/usr/bin/python3


"""
Module that defines a BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer validation
    """

    def area(self):
        """
        Public instance method that raises an exception
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
