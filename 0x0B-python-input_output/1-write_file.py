#!/usr/bin/python3

"""Define and write a text file function."""


def write_file(filename="", text=""):
    """writes a string to a text file UTF8 character.
    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.
    Returns:
        the number of characters to be written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
