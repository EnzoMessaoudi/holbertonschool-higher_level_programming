#!/usr/bin/python3


"""
Modulo that check if an instance belong to a class or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Function that check if an object belong to a subclass
    """
    return isinstance(obj, a_class)
