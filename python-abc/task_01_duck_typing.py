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
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return abs((self.width + self.height) * 2)


def shape_info(value):
    print("Area: {}".format(value.area()))
    print("Perimeter: {}".format(value.perimeter()))
