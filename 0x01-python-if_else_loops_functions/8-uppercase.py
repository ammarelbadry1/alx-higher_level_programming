#!/usr/bin/python3
def uppercase(str):
    for i in str:
        isLower = True if ord(i) >= 97 and ord(i) <= 122 else False
        print("{}".format(chr(ord(i) - 32) if isLower else i), end="")
    print()
