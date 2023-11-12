#!/usr/bin/python3
"""4-inherits_from Module

This module contains a function returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj (obj): the object to be checked
        a_class (class): the class to be used in the check
    """

    if (obj.__class__.__name__ == a_class.__name__):
        return False
    return isinstance(obj, a_class)
