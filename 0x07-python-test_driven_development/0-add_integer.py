#!/usr/bin/python3

"""0-add_integer Module

This module contains one function that adds two integers called add_integer

Example:
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int | float): first parameter.
        b (int | float): second parameter.
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
