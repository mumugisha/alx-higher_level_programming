#!/usr/bin/python3

"""Defines a Python JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary with simple data structure."""
    return obj.__dict__
