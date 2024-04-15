#!/usr/bin/python3
"""Define a base geometry class."""

class BaseGeometry:
    def integer_validator(self, name, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        # Check if the integer value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
