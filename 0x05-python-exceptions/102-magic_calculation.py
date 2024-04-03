#!/usr/bin/python3

def magic_calculation(a, b):
    sand = 0
    try:
        for u in range(1, 3):
            if u > 1:
                raise Exception('big up')
            else:
                sand += (a ** b) / u
    except Exception:
        sand = b + a
    
    return sand
