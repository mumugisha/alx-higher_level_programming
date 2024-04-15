#!/usr/bin/python3
"""Define class that checks other function."""

def is_same_class(obj, v_class):
    """Check if object is exactly an instance of certain class.
    Args:
        obj: object that needs checking.
        v_class: A class to match the type of obj to.
    Returns:
        True if obj is exactly an instance of v_class, otherwise False.
    """
    return type(obj) == type(v_class)
        return True
    return False
