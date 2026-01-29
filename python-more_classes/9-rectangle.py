#!/usr/bin/python3


"""
Modulo that return the width and height of the rectangle
"""


class Rectangle:
    """
    Class that get the height and width of a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        use __init__ to pick what the user want for values
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Get the value of width
        """
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        """
        Set the value of width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width

    @property
    def height(self):
        """
        Get the value of height
        """
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        """
        Set the value of height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

    def area(self):
        """
        What's the area of the rectangle is
        """
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """
        What's the perimeter of the rectangle is
        """
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__height + self._Rectangle__width) * 2

    def __str__(self):
        """
        Print a rectangle with the view of a users
        """
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        lines = []
        for i in range(self._Rectangle__height):
            lines.append("{}".format(self.print_symbol)
                         * self._Rectangle__width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Print a rectangle with the view of a developper
        """
        return (
            f"Rectangle({self._Rectangle__width}, "
            f"{self._Rectangle__height})"
        )

    def __del__(self):
        """
        Print this line if the user destroy the rectangle
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
