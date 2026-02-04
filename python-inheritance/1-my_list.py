#!/usr/bin/python3


"""
Modulo that permit to a class to inherit from another
"""


class MyList(list):
    """
    MyList inherit from a list and can print a list in order
    """
    def print_sorted(self):
        """
        Print a sorted list
        """
        if self == []:
            return
        print(sorted(self))
