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
