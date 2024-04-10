#!/usr/bin/python3
""" this is class locked attributes """


class LockedClass:
    """ do not initiate another lockedClass, but only 'first_name'.
    """
    __slot__ = ["first_name"]
