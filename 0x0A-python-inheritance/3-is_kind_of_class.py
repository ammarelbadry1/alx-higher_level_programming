#!/usr/bin/python3
"""3-is_kind_of_class Module

This module contains a function returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj (obj): the object to be checked
        a_class (class): the class to be used in the check
    """

    return isinstance(obj, a_class)
