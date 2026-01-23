#!/usr/bin/python3


"""
Modulo that print a square
>>> print_square(1)
#
"""


def print_square(size):
    """
    Function that print a square with a lenght of size
    """
    if size == "":
        raise ValueError("size must be an integer")
    elif size == 0:
        return
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
