#!/usr/bin/python3
"""7-add_item Module

This module contains a script that adds all arguments to a Python list,
and then save them to a file.
"""

if __name__ == "__main__":
    import sys
    import os

    save_file = __import__("5-save_to_json_file").save_to_json_file
    load_file = __import__("6-load_from_json_file").load_from_json_file

    if os.path.exists("add_item.json"):
        file_content = load_file("add_item.json")
    else:
        file_content = []
    my_args = sys.argv[1:]
    file_content += my_args
    save_file(file_content, "add_item.json")
