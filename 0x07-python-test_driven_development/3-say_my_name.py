#!/usr/bin/python3

"""3-say_my_name Module

This module contains one function that prints "My name is
<first name> <last name>"

Example:
    >>> say_my_name = __import__('3-say_my_name').say_my_name
    >>> say_my_name("John", "Doe")
    My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): first argument
        last_name (str): second argument
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
