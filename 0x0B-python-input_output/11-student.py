#!/usr/bin/python3
"""Define a Student class."""


class Student:
    """Represent a student class."""

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

    def to_json(self, attrs=None):
        """list of strings, only attributes name contain in this list must be retrieved.
        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student class.
        Args:
            json (dict): The key value  of pairs to replaces all attributes of the student class.
        """
        for v, w in json.items():
            setattr(self, v, w)
