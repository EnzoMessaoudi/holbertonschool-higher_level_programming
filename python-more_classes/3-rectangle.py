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
        return self._Rectangle__width

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
        return self._Rectangle__height

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

    def area(self):
        """
        What's the area of the rectangle is
        """
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """
        What's the perimeter of the rectangle is
        """
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__height + self._Rectangle__width) * 2

    def __str__(self):
        """
        Print a rectangle with the view of a users
        """
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        lines = []
        for i in range(self._Rectangle__height):
            lines.append("#" * self._Rectangle__width)
        return "\n".join(lines)

    def __repr__(self):
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        """
        Print a rectangle with the view of a developper
        """
        return "{}, {}".format(self._Rectangle__height, self._Rectangle__width)
