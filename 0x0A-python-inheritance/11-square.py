#!/usr/bin/python3

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
        super().__init__(side_length, side_length)


s = Square(13)
print("[Square] {}/{}".format(s.width, s.height))
print(s.area())
