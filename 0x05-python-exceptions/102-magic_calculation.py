#!/usr/bin/python3
import sys

def magic_calculation(a, b):
    sand = 0
    for u in range(1, 2):
        try:
            if u > a:
                raise Exception('big up')
            else:
                sand += (a ** b) / u
        except Exception:
            sand = b + a
            break
    return sand
