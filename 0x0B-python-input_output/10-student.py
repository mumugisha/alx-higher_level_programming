class Student:
    """Represent a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student class.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return JSON representation of the instance.
        
        Args:
            attrs (list): The list of attributes to represent a student.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict___
