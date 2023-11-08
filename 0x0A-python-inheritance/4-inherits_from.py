#!/usr/bin/python3
"""
This module for inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
