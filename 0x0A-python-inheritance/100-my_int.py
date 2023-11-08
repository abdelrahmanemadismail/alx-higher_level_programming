#!/usr/bin/python3
"""
Module for MyInt class
"""


class MyInt(int):
    """
    A class for a custom integer type with inverted equality operators.

    Methods:
        __eq__(self, other): Inverts the equality operator (==).
        __ne__(self, other): Inverts the inequality operator (!=).
    """
    def __eq__(self, other):
        """
        Inverts the equality operator (==).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator (!=).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
