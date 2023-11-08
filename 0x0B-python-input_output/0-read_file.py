#!/usr/bin/python3
"""0-read_file Module.

This module contains one function that reads a file
"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename (str): file path
    """

    with open(filename, encoding="utf-8") as f:
        data_read_count = f.read()
        print(data_read_count, end="")
