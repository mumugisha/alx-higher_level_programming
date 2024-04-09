#!/usr/bin/python3
"""define a Rectangle class."""


class Rectangle:
    """Represents a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new group of Rectangle class.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width attributes set"""
        if not isinstance(value, int):
            raise TypeError("width must is an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attributes set"""
        if not isinstance(value, int):
            raise TypeError("height must is an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        def __str__(self):
            """Return and print the representation of the Rectangle.
            Represent rectangle with # character.
            """
            if self.__width == 0 or self.__height == 0:
               return ""
            rect = []

            for a in range(self.__height):
                [rect.append('#') for b in range(self.__width)]
                if a != self.__height - 1:
                    rect.append("\n")
                    return "".join(rect)
