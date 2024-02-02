#!/usr/bin/python3
"""This script takes in a URL,
sends a request to the URL and displays the body of the response,
if the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    status_code = response.status_code

    if status_code >= 400:
        print("Error code:", status_code)
    else:
        print(response.text)
