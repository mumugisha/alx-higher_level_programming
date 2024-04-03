#!/usr/bin/python3

import sys

def magic_calculation(a, b):
    sand = 0
    try:
        if a < 1:
            raise ValueError('a must be at least 1')
        else:
            for u in range(1, 2):
                sand += (a ** b) / u
    except ValueError:
        sand = b + a
    return sand

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(magic_calculation(a, b))
    except IndexError:
        print("Usage: python3 script.py <a> <b>")
    except ValueError:
        print("Both 'a' and 'b' must be integers.")
