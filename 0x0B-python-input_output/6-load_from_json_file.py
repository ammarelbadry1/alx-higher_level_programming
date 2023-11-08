#!/usr/bin/python3
"""6-load_from_json_file Module.

This module contains one function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): the object to be saved
        filename (str): the file path where to save
    """

    with open(filename) as f:
        return json.load(f)
