#!/usr/bin/python3
"""
This module provides a function for loading an object from a JSON file.

Usage:
- Import this module using 'import load_from_json_file_module'
- Call the load_from_json_file function with the filename.
"""


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to load the object from.

    Returns:
    - object: The Python object loaded from the JSON file.

    Note:
    - This function uses the 'with' statement to ensure proper handling of the
      file stream.
    - Exceptions are not explicitly managed if the JSON file doesn't represent
      an object.
    - permission or file doesn't exist exceptions are not explicitly managed
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
