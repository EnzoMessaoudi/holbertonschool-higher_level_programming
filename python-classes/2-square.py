#!/usr/bin/python3


"""
This module create a square with a size but check if it's negative or an int
"""


class Square:
    def __init__(self, size=0):
        """
        Create a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._square__size = size
