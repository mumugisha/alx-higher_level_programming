#!/usr/bin/python3
"""Define class that checks other function."""

def is_same_class(obj, v_class):
    """Check if object is exactly an instance of certain class.
    Args:
        obj: object that need checking.
        v_class: A class to match a type of obj to define.
    Returns:
        If obj is exactly an instance of v_class - True.
        Otherwise - False.
    """
    if type(obj) == v_class:
        return True
    return False
