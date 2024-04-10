#!/usr/bin/python3
"""I define Locked Class"""

class LockedClass:
    """do not initiate another lockedClass, but only 'first_name'.
    """
    __slot__ = ["first_name"]
