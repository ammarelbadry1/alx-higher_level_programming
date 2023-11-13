#!/usr/bin/python3
"""6-load_from_json_file Module

This contains a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): the file path we would read from it.
    """

    with open(filename, "r") as f:
        return json.load(f)
