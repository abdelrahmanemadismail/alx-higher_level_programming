#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """
    An empty class to represent a base geometry.

    Methods:
        area(self): Raises an Exception with the message
        "area() is not implemented".
    """
    def area(self):
        """
        Placeholder method to be implemented by subclasses.

        Raises:
            Exception: Always raises an Exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value provided as an argument.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
