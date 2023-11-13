#!/usr/bin/python3
"""12-pascal_triangle Module

This module contains a function that returns
a list of lists of integers representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n.

    Args:
        n (int): the number of triangle rows.
    """

    pascal = []
    if (n <= 0):
        return pascal
    for i in range(n):
        tmp = []
        tmp.append(1)
        for j in range(1, i):
            tmp.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
        if (i != 0):
            tmp.append(1)
        pascal.append(tmp)
    return pascal
