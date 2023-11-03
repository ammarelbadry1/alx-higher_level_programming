#!/usr/bin/python3

"""4-print_square Module

This Module contains one function that prints a square with the character #

Example:
    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(3)
    ###
    ###
    ###
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): the size of the square
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
