#!/usr/bin/python3
"""4-from_json_string Module

This module contains a function that returns
an object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): the json string to be deserialized.
    """

    return json.loads(my_str)
