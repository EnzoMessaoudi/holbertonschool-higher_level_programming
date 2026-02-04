#!/usr/bin/python3


"""
Modulo that uses Duck Typing
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        if not isinstance(radius, int) and radius <= 0:
            raise ValueError("radius must be a positive integrer")
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        if not isinstance(width, int) and width <= 0:
            raise ValueError("width must be a positive integer")
        if not isinstance(height, int) and height <= 0:
            raise ValueError("height must be a positive integer")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(value):
    print("Area: {}".format(value.area()))
    print("Perimeter: {}".format(value.perimeter()))
