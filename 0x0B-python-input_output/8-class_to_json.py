#!/usr/bin/python3
"""8-class_to_json Module

This module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure:
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj (dict): the object to be serialized.
    """

    return obj.__dict__
