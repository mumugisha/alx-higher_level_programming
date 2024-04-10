#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent user for initiating new LockedClass attribute
    for anything other than called 'first_name'.
    """

    __slots__ = ["first_name"]
