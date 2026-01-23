#!/usr/bin/python3


"""
This modulo print a string but with a new line after ./?/:
>>> text_indentation("Coucou")
Coucou
"""


def text_indentation(text):
    """
    Function that print text but with a new line after each ./?/:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
