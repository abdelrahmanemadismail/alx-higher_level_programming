#!/usr/bin/python3
"""
This module provides a function for converting a JSON string to Python object.

Usage:
- Import this module using 'import from_json_string_module'
- Call the from_json_string function with the desired JSON string.
"""


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string to be converted to a Python object.

    Returns:
    - object: The Python object represented by the JSON string.

    Note:
    - Exceptions are not explicitly managed if the JSON string
    doesn't represent an object.
    """
    import json
    return json.loads(my_str)
