#!/usr/bin/python3

"""Define a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """I intialize a new Rectangle.
        Args:
            width (int): The width of new Rectangle.
            height (int): The height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() that represents a new Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
