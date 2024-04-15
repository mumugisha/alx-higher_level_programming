#!/usr/bin/python3
"""Define a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.

    Returns:
        bool: True if obj is an instance or inherits instance of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
