#!/usr/bin/python3

"""Define a Rectangle sub Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a new square class."""

    def __init__(self, size):
        """I initialize a new square.
        Args:
            size (int): The size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
