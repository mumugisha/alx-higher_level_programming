#!/usr/bin/python3
"""Define class that checks other function."""

def is_same_class(obj, a_class):
    """Check if object is exactly an instance of certain class.
    Args:
        obj: object that need checking.
        a_class: A class to match a type of obj to define.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
