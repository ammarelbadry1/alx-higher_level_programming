#!/usr/bin/python3
"""3-to_json_string Module.

This module contains one function that returns the JSON
representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Serialize python data

    Args:
        my_obj (dict): the object to be serialized
    """

    return json.dumps(my_obj)
