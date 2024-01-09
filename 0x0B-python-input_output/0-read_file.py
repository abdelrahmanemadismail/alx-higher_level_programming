#!/usr/bin/python3
"""
This module contains a function to read a file and print its content to stdout

Usage:
- Import this module using 'import your_module_name'
- Call the read_file function with the desired filename.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Parameters:
    - filename (str): name of the file to be read. Defaults to an empty string

    Note:
    - This function uses 'with' statement to ensure proper handling of file.
    - permission or non-existent file exceptions are not explicitly managed.
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
