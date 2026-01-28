#!/usr/bin/python3


"""
This module create a square with a size but check if it's negative or an int
"""


class Square:
    """
    Create a square and verify its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Check the size and position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the value of position
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Check the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
