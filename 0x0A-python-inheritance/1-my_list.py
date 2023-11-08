#!/usr/bin/python3
"""
This module
"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
