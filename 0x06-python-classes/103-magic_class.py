#!/usr/bin/python3
"""This code defines a MagicClass matching exactly a bytecode provided by Holberton."""
import math

class MagicClass:
    """This class represents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of MagicClass.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
