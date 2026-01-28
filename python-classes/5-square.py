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
        self.size = size

    @property
    def size(self):
        """
        Used to get the value size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Used to set the value size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Check the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()