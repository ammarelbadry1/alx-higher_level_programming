#!/usr/bin/python3
def print_square(size):
    try:
        if (size < 0):
            raise Exception
    except Exception:
        print("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        if (i != size - 1):
            print()
