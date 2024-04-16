class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side_length):
        # Call the superclass's __init__ method with side_length as both width and height
        super().__init__(side_length, side_length)
