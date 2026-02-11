#!/usr/bin/python3

"""
Modulo that read a file
"""


def read_file(filename=""):
    """
    Function that read a file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
