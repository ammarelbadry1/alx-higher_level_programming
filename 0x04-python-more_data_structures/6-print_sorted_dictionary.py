#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{}: ".format(i), end="")
        print("{}".format(a_dictionary[i]))
