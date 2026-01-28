#!/usr/bin/python3


"""
This module create a square with a size but check if it's negative or an int
"""


class Square:
    """
    Create a square and verify its size
    """
    def __init__(self, size=0):
        """
        Check the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """
        Check the area of the square
        """
        area = self._Square__size * self._Square__size
        return area
