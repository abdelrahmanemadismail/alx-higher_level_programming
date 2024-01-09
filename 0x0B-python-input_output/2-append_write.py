#!/usr/bin/python3
"""
This module provides a function for appending a string to the end of
a text file (UTF8).

Usage:
- Import this module using 'import append_write_module'
- Call the append_write function with the desired filename and text.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number
    of characters added.

    Parameters:
    - filename (str): The name of the file to append. Defaults to empty string
    - text (str): string to be appended to file. Defaults to an empty string.

    Returns:
    - int: The number of characters added to the file.

    Note:
    - This function uses the 'with' statement to ensure proper handling of the
      file stream.
    - If the file doesn't exist, it is created.
    - permission or file doesn't exist exceptions are not explicitly managed.
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        characters_added = f.write(text)

    return characters_adde
