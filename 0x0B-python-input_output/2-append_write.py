#!/usr/bin/python3
"""2-append_write Module.

This module contains one function that writes to the end of a file
"""


def append_write(filename="", text=""):
    """Writes to the end a file

    Args:
        filename (str): file path
        text (str): text to be written
    """

    with open(filename, "a", encoding="utf-8") as f:
        data_written_count = f.write(text)
    return data_written_count
