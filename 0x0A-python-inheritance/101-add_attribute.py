#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    setattr(obj, attribute, value)

"""Define a function that and adds attribute."""

def add_attribute(obj, att, value):
    """Add another new attribute to obj if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

