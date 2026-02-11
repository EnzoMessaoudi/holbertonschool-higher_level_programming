#!/usr/bin/python3
"""
Modulo that serialize and deserialize using pickles
"""
import pickle


class CustomObject:
    """
    python class
    """
    def __init__(self, name="John", age=25, is_student=True):
        """
        Find the attributes of the class
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a boolean")

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the class
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("is_student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        serialize filename
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize filename
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if not isinstance(obj, cls):
                    raise TypeError("Invalid object type in pickle file")
                return obj
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, OSError):
            return None
