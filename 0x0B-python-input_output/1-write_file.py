#!/usr/bin/python3
"""
This module provides a function for writing a string to a text file (UTF8).

Usage:
- Import this module using 'import write_file_module'
- Call the write_file function with the desired filename and text.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters
    written.

    Parameters:
    - filename (str): The name of the file to write. Defaults to empty string.
    - text (str): The string to be written to the file. Defaults to an empty
      string.

    Returns:
    - int: The number of characters written to the file.

    Note:
    - This function uses the 'with' statement to ensure proper handling of the
      file stream.
    - File permission exceptions are not explicitly managed.
    - The function creates the file if it doesn't exist and overwrites its
      content if it already exists.
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        characters_written = f.write(text)

    return characters_written
