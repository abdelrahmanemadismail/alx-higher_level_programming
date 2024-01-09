#!/usr/bin/python3
"""
This module provides a function for converting an instance of a class to a
dictionary with simple structures (list, dictionary, string, integer, boolean)
for JSON serialization.

Usage:
- Import this module using 'import class_to_json_module'
- Call the class_to_json function with an instance of a class.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object.

    Parameters:
    - obj: An instance of a class.

    Returns:
    - dict: A dictionary representing the object with simple data structures.

    Note:
    - The function assumes that all attributes of the class are serializable.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
