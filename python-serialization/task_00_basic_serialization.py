#!/usr/bin/python3

"""
Modulo that serialize and deserialize
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    Function that serialize
    """
    with open(filename, "w") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Function that deserialize
    """
    with open(filename, "r") as file:
        return pickle.load(file)
