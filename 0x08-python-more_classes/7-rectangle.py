#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): Number of Rectangle class instances.
        print_symbol (any): Symbol used of string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """I initialize a new Rectangle class.

        Args:
            width (int): Width of new rectangle class.
            height (int): Height of new rectangle class.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of Rectangle class."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of Rectangle class."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle class."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of Rectangle class."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of Rectangle class.

        Represent rectangle class with a character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for a in range(self.__height):
            [rect.append(str(self.print_symbol)) for b in range(self.__width)]
            if a != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string that represent a Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deleted Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
