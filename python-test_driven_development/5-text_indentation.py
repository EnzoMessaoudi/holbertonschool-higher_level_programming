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
    elif text == "":
        raise ValueError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
