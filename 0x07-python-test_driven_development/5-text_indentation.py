#!/usr/bin/python3

"""5-text_indentation Module

This module contains one function that prints a text with 2 new lines
after each of these characters: ., ? and :

Example:
    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("How do you feel?I feel happy.")
    How do you feel?
    <BLANKLINE>
    I feel happy.
    <BLANKLINE>
"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): the text to be printed.
    """

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    text_len = len(text)
    i = 0
    flag = 1
    while i < text_len:
        current = text[i]
        if (current == " " and flag):
            i += 1
            continue
        if (current == '.' or current == '?' or current == ':'):
            flag = 1
            print(current)
            print()
            i += 1
            continue
        flag = 0
        print(current, end="")
        i += 1
