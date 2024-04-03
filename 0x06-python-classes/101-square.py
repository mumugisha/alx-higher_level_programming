class Square:
    """A class to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be >= 0.")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("Position must be a tuple of 2 positive integers.")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' character."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """String representation of the square."""
        if self.__size == 0:
            return ""

        sand = ""
        for _ in range(self.__position[1]):
            sand += "\n"

        for _ in range(self.__size):
            sand += " " * self.__position[0]
            sand += "#" * self.__size
            sand += "\n"

        return sand
