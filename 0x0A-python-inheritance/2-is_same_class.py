#!/usr/bin/python3
"""2-is_same_class Module

This module contains a function returns True if the object
is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """returns True if the object
    is exactly an instance of the specified class ; otherwise False.

    Args:
        obj (obj): the object to be checked
        a_class (class): the class to be used in the check
    """

    return obj.__class__.__name__ == a_class.__name__
