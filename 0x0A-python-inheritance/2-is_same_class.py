#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
