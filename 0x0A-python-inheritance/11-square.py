#!/usr/bin/python3

"""Definea a Rectangle that inherits from a Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    """Represents a square class."""
