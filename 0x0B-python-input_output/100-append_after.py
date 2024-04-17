#!/usr/bin/python3
""" Define a function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string.
    Args:
        filename (str): The name of text file.
        search_string (str): The string to search for within the taxt file.
        new_string (str): The string to insert a text line.
    """
    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write:
        write.write(text)
