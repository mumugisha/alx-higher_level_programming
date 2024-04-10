#!/usr/bin/python3
"""Define Rectangle class."""


class Rectangle:
    """Represent a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle class.

        Args:
            width (int): The width of new rectangle class.
            height (int): The height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of the Rectangle."""
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
        """set height of the Rectangle class."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
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
        """Return printable representation of Rectangle.

        Represent rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for a in range(self.__height):
            [rect.append('#') for b in range(self.__width)]
            if a != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
