#!/usr/bin/python3


"""
Module that defines MyList class which inherits from list
"""

__all__ = ["MyList"]


class MyList(list):
    """MyList class that inherits from list and can print a sorted list"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it"""
        print(sorted(self))
