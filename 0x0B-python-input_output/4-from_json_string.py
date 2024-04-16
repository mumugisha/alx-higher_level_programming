#!/usr/bin/python3

"""Define a JSON string function."""
import json


def from_json_string(my_str):
    """Return Python object that represent JSON string."""
    return json.loads(my_str)
