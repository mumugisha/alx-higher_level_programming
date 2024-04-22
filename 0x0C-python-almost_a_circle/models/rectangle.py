#!/usr/bin/python3
"""Define the rectangle class model."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class model."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """I initialize a new Rectangle class model.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute value.
                - 1st argument represent the id attributes
                - 2nd argument represent the width attributes
                - 3rd argument represent the height attributes
                - 4th argument represent x attribute
                - 5th argument represent y attribute
            **kwargs (dict): New key value pairs of the attributes.
        """
        if args and len(args) != 0:
            u = 0
            for arg in args:
                if u == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif u == 1:
                    self.width = arg
                elif u == 2:
                    self.height = arg
                elif u == 3:
                    self.x = arg
                elif u == 4:
                    self.y = arg
                u += 1

        elif kwargs and len(kwargs) != 0:
            for c, d in kwargs.items():
                if c == "id":
                    if d is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = d
                elif c == "width":
                    self.width = d
                elif c == "height":
                    self.height = d
                elif c == "x":
                    self.x = d
                elif c == "y":
                    self.y = d

    def to_dictionary(self):
        """Return the dictionary to represent Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() that represent Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
