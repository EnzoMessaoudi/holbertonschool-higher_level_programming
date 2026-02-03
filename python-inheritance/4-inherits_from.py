#!/usr/bin/python3


"""
Modulo that check if an instance inherited from the class
"""


def inherits_from(obj, a_class):
    """
    check if obj inherited from a_class
    """
    return type(obj) is not a_class
