#!/usr/bin/python3
"""
Module for Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class for representing squares, inheriting from Rectangle.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
