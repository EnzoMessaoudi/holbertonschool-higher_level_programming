#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attr_order = ["age", "last_name", "first_name"]
        result = {}

        if attrs is None:
            for attr in attr_order:
                result[attr] = getattr(self, attr)
        else:
            for attr in attr_order:
                if attr in attrs:
                    result[attr] = getattr(self, attr)

        return result

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
