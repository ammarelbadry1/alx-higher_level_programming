#!/usr/bin/python3
"""1-my_list Module

Defines a MyList class.
"""


class MyList(list):
    """Represent a MyList class."""

    def print_sorted(self):
        """Print sorted array."""
        s_list = self[:]
        s_list.sort()
        print(s_list)
