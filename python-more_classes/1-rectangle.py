#!/usr/bin/python3


"""
Modulo that return the width and height of the rectangle
"""


class Rectangle:
    """
    Class that get the height and width of a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        use __init__ to pick what the user want for values
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the value of width
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Set the value of width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width

    @property
    def height(self):
        """
        Get the value of height
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Set the value of height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height
