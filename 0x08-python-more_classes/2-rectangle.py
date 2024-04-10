#!/usr/bin/python3
"""I define Rectangle class."""

class Rectangle:
    """This is a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width (int): The  Width of new rectangle.
            height (int): The Height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width attribute of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
