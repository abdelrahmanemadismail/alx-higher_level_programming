#!/usr/bin/python3
"""
This module provides a function 'pascal_triangle' that returns a list
of lists of integers representing Pascal's triangle of n.

Usage:
- Import this module using 'from pascal_triangle_module import pascal_triangle'
- Call the pascal_triangle function with an integer n to get the triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate.

    Returns:
    - list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle
