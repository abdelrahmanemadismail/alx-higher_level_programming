#!/usr/bin/python3
"""
Module for Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class for representing rectangles, inheriting from BaseGeometry.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.
        area(self): Calculates the area of the rectangle.
        __str__(self): Provides custom string representation of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Provides a custom string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
