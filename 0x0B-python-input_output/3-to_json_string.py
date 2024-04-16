#!/usr/bin/python3

"""Define string to JSON's function."""
import json


def to_json_string(my_obj):
    """Return JSON  to represent a string object."""
    return json.dumps(my_obj)
