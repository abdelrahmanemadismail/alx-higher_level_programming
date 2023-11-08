#!/usr/bin/python3
"""
This module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of
    a class that inherited from, a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited from a_class.
    """
    return isinstance(obj, a_class)
