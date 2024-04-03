#!/usr/bin/python3

def safe_print_division(a, b):
    sand = None
    try:
        sand = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(sand))
    return sand
