#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        sand = fct(*args)
        return sand
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
    return None
