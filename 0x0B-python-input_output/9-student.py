#!/usr/bin/python3
"""Define a class Student by specialization."""


class Student:
    """Represent a class of student."""

    def __init__(self, first_name, last_name, age):
        """I initialize a new Student.
        Args:
            first_name (str): The first name of the student class.
            last_name (str): The last name of the student class.
            age (int): The age of the student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a class of student."""
        return self.
