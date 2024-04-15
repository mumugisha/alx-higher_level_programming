#!/usr/bin/python3

"""Class mylist that inherits from List."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a sorted list in ascending order."""
        print(sorted(self))
