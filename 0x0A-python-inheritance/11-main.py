#!/usr/bin/python3
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def __str__(self):
        return f'Square with side length {self.side_length}'

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print("Area:", s.area())
