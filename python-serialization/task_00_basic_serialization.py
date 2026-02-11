#!/usr/bin/python3

"""
Modulo that serialize and deserialize
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function that serialize
    """
    with open(filename, "wb", encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Function that deserialize
    """
    with open(filename, "rb", encoding='utf-8') as file:
        return json.load(file)
