#!/usr/bin/python3
"""
Module that defines MyList class, which inherits from list
"""

class MyList(list):
    """MyList inherits from list and can print a sorted list"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it"""
        print(sorted(self))

    def append(self, item):
        """Append only if item is an integer"""
        if not isinstance(item, int):
            raise TypeError("Only integers can be added")
        super().append(item)

    def extend(self, iterable):
        """Extend only with integers"""
        for item in iterable:
            if not isinstance(item, int):
                raise TypeError("Only integers can be added")
        super().extend(iterable)

    def insert(self, index, item):
        """Insert only if item is an integer"""
        if not isinstance(item, int):
            raise TypeError("Only integers can be added")
        super().insert(index, item)
