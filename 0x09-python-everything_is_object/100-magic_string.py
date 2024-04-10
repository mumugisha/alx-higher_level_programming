#!/usr/bin/python3
def magic_string():
    magic_string.numb = getattr(magic_string, 'numb', 0) + 1
    return ("BestSchool, " * (magic_string.numb - 1) + "BestSchool")
