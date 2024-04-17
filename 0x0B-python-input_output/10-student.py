#!/usr/bin/python3
"""Define a student class."""


class Student:
    """Represent a student class."""

    def __init__(self, first_name, last_name, age):
        """I initialize a new Student class.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """list of strings and attribute names contained in this list must be retrieved.
        Args:
            attrs (list): The attribute to represent a student.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}
        return self.__dict__
