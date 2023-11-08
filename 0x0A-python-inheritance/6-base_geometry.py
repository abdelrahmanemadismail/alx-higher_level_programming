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
