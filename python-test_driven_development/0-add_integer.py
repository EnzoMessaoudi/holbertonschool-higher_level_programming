#!/usr/bin/python3


"""
modulo that takes two integer (a and b) and add them
>>> add_integer(2, 2)
4
"""


def add_integer(a, b=98):
    """
    This function is use to adds 2 integers together
    """
    if a == "":
        raise ValueError("a must be an integer")
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
        return a + b
    else:
        raise TypeError("b must be an integer")
