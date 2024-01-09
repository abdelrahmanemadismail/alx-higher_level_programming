#!/usr/bin/python3
"""
This module provides a function 'append_after' that inserts a line of text
to a file after each line containing a specific string.

Usage:
- Import this module using 'from append_after_module import append_after'.
- Call the append_after function with the filename, search_string, new_string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific str

    Parameters:
    - filename (str): The name of the file.
    - search_string (str): The string to search for in each line.
    - new_string (str): line to insert after each line containing search str.

    Note:
    - Uses the 'with' statement to ensure proper handling of the file stream.
    - permission or non-existent file exceptions are not explicitly managed.
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
