#!/usr/bin/python3
"""1-write_file Module.

This module contains one function that writes to a file
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename (str): file path
        text (str): text to be written
    """

    with open(filename, "w", encoding="utf-8") as f:
        data_written_count = f.write(text)
    return data_written_count
