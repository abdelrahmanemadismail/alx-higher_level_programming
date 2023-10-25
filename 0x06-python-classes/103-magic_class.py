#!/usr/bin/python3
"""
This module defines a class MagicClass.
"""


import math


class MagicClass:
    """
    MagicClass mimics the behavior of the bytecode.

    This class validates and stores a radius value and provides methods to
    calculate the area and circumference based on the radius.

    Attributes:
        __radius (int or float): The radius of the circle.

    Methods:
        __init__(self, radius): Initialize MagicClass with a radius value.
        area(self): Calculate the area of the circle.
        circumference(self): Calculate the circumference of the circle.
    """
    def __init__(self, radius=0):
        """
        Initialize MagicClass with a radius value.

        Args:
            radius (int or float): The radius value for the circle.

        Raises:
            TypeError: If the provided radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
