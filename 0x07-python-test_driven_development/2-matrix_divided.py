#!/usr/bin/python3

"""2-matrix_divided Module

This module contains one function that divides all elements of a matrix
rounded to 2 decimal places and return a new_matrix

Example:
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): the matrix to be divided
        div (int | float): the divisor
    """

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    e = TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (matrix == [] or not isinstance(matrix[0], list)):
        raise e
    row_size = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if (not isinstance(i, list)):
            raise e
        if (len(i) != row_size):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in i:
            if (not isinstance(j, int) and not isinstance(j, float)):
                raise e
            row.append(round(j / div, 2))
        new_matrix.append(row)
    return new_matrix
