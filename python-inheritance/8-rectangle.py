#!/usr/bin/python3


"""
Modulo that write a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
