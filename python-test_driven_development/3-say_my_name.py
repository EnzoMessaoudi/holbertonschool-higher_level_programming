#!/usr/bin/python3


"""
This modulo print the name passed by the user
>>> say_my_name("Walter", "White")
My name is Walter White
"""


def say_my_name(first_name, last_name=""):
    """
    Function that takes two string and print them
    """
    if first_name == "":
        raise ValueError("first_name must be a string")
    elif not isinstance(first_name, str) and not "":
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
