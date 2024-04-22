#!/usr/bin/python3
"""Define a square class model."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represent a square model."""

    def __init__(self, size, x=0, y=0, id=None):
        """I initialize a new Square model.

        Args:
            size (int): The size of the new Square model.
            x (int): The x coordinate of the new Square model.
            y (int): The y coordinate of the new Square model.
            id (int): The identity of the new Square model.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square model.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key value pairs of attributes.
        """
        if args and len(args) != 0:
            u = 0
            for arg in args:
                if u == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif u == 1:
                    self.size = arg
                elif u == 2:
                    self.x = arg
                elif u == 3:
                    self.y = arg
                u += 1

        elif kwargs and len(kwargs) != 0:
            for c, d in kwargs.items():
                if c == "id":
                    if d is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = d
                elif c == "size":
                    self.size = d
                elif c == "x":
                    self.x = d
                elif c == "y":
                    self.y = d

    def to_dictionary(self):
        """Return the dictionary that represent the Square model."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() that represent the Square model."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
