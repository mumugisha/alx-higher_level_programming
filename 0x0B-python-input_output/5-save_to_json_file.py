#!/usr/bin/python3

"""Define and writes an Object to a text file function."""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file JSON character."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
