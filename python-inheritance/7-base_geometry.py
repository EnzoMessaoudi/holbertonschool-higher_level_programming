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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
