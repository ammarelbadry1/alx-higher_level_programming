#!/usr/bin/python3
"""4-from_json_string Module.

This module contains one function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Deserialize python data

    Args:
        my_str (str): the string object to be deserialized
    """

    return json.loads(my_str)
