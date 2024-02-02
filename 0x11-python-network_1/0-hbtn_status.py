#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        content_type = (response.headers.get_content_charset()).lower()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        if (content_type == "utf-8"):
            print("\t- utf8 content: OK")
