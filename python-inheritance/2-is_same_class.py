#!/usr/bin/python3


"""
Modulo that check if an object is a instance of an exact class
"""


def is_same_class(obj, a_class):
    """
    Return true if obj is an instance of a_class
    """
    return type(obj) is a_class
