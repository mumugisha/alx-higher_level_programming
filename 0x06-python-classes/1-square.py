#!/usr/bin/python3

"""Defines a class Square"""

class Square:
    """A class with a private instance attribute"""

    def __init__(self, size):
        """Initialize a new Square object
        
        Args:
            size (int): size of new square.
        """
        self.__size = size
