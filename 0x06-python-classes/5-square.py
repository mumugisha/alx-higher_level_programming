#!/usr/bin/python3
# Project by Mugisha
"""Defines a Square class"""

class Square:
    """This class represents a square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self._size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self._size = value

    def area(self):
        """Return the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square using # character."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
