#!/usr/bin/python3
"""5-save_to_json_file Module.

This module contains one function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): the object to be saved
        filename (str): the file path where to save
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
