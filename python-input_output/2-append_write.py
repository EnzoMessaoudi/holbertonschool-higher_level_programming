#!/usr/bin/python3

"""
Modulo that write inside of a file
"""


def append_write(filename="", text=""):
    """
    Function  that append text at the end of filename
    """
    with open(filename, 'a') as file:
        file_len = file.write(text)
        return file_len
