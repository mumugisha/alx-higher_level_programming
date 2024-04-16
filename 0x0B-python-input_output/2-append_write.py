#!/usr/bin/python3

"""Define a text file appended function."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file UTF8 character.
    Args:
        filename (str): The name of the file to be appended to.
        text (str): The string to be appended to file.
    Returns:
        The number of characters be appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
