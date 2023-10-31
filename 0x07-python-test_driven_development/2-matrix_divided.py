#!/usr/bin/python3


"""
matrix_divided - A module for dividing elements of a matrix by a given divisor
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor (a number that is not zero).

    Returns:
        matrix: with elements divided by divisor rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to 0.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    f0 = not isinstance(matrix, list)
    f1 = not all(isinstance(row, list) for row in matrix)
    f2 = not all(isinstance(i, (int, float)) for row in matrix for i in row)
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if f0 or f1 or f2:
        raise TypeError(s)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
