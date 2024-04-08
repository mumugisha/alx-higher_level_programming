#!/usr/bin/python3
""" I define a group, Rectangle class."""

class Rectangle:
    """ This is a rectangle class"""

    def __init__(self, width=0, height=0):
        """ Initialize new group Rectable.

        Args:
            width (int): Width arguments of rectangle.
            height (int): Height arguments of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Make a class of rectangle Width attributes."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width attributes set"""
        if not isinstance(value, int):
            raise TypeError("width is an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Make a class of rectangle Height attributes."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Height attributes set"""
        if not isinstance(value, int):
            raise TypeError("height is an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
