#!/usr/bin/python3
"""This script takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post("http://0.0.0.0:5000/search_user", data=q)

    try:
        result = response.json()
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result["id"], result["name"]))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
