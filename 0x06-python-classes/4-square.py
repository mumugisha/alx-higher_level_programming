#!/usr/bin/python3

"""Define Square class"""

class Square:
    """This class represents a square"""

    def __init__(self, side_length=0):
        """Initialize a new square.

        Args:
            side_length (int): The length of each side of the square.
        """
        if not isinstance(side_length, int):
            raise TypeError("Side length must be an integer")
        elif side_length < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = side_length

    @property
    def side_length(self):
        """Get the length of each side of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, sand):
        """Set the length of each side of the square.

        Args:
            sand (int): The new length of each side of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(sand, int):
            raise TypeError("Side length must be an integer")
        elif sand < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = sand

    def area(self):
        """Calculate and return the area of the square."""
        return self.__side_length ** 2
