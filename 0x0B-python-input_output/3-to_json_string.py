#!/usr/bin/python3
"""
This module provides a function for converting an object to
its JSON representation.

Usage:
- Import this module using 'import to_json_string_module'
- Call the to_json_string function with the desired object.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object.

    Note:
    - Exceptions are not explicitly managed if the object can't be serialized.
    """
    import json
    return json.dumps(my_obj)
