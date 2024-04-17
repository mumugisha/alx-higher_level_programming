#!/usr/bin/python3

"""Define an object from JSON file function."""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file."""
    with open(filename) as file:
        return json.load(file)
