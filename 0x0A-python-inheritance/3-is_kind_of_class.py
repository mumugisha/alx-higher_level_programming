#!/usr/bin/python3
"""Define a class and inherited class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is inherited instance of a class.
    Args:
        obj (any): object to check.
        a_class (type): class to match a type of obj to.
    Returns:
        If obj is instance or inherits instance of this a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
