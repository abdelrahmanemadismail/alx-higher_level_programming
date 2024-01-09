#!/usr/bin/python3
"""
This module provides a class 'Student' that defines a student with public
instance attributes and methods for JSON serialization and deserialization.

Usage:
- Import this module using 'from student_module import Student'.
- Create instances of the Student class with first_name, last_name, and age.
- Call the to_json method to retrieve the dictionary representation.
- Call the reload_from_json method to replace all attributes from a dictionary.
"""


class Student:
    """
    Represents a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): A list of strings representing the attribute names
        to retrieve. If None, all attributes are retrieved.

        Returns:
        - dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Parameters:
        - json (dict): A dictionary with attribute names as keys and
        corresponding values.

        Note:
        - Assumes json will always be a dictionary.
        - A dictionary key is the public attribute name.
        - A dictionary value is the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
