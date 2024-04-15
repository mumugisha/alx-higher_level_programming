#!/usr/bin/python3
"""Define a function to check inheritance."""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class.
    
    Args:
        obj: The object to check.
        a_class (type): The class to check against.
    
    Returns:
        bool: True if obj inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
	return True
    return False
