#!/usr/bin/python3
"""
This module provides a function for saving an object to a text file using
a JSON representation.

Usage:
- Import this module using 'import save_to_json_file_module'
- Call the save_to_json_file function with the object and the filename.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
    - my_obj: The object to be saved to the file.
    - filename (str): The name of the file to save the object to.

    Note:
    - This function uses the 'with' statement to ensure proper handling of the
      file stream.
    - Exceptions are not explicitly managed if the object can't be serialized.
    - File permission exceptions are not explicitly managed.
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
