#!/usr/bin/python3
"""3-to_json_string Module

This module contains a function that  returns
the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj (object): the object to be serialized.
    """

    return json.dumps(my_obj)
