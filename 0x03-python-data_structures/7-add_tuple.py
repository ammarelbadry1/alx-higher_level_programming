#!/usr/bin/python3
def insert_zeros(_tuple):
    if (len(_tuple) == 1):
        _tuple = _tuple[0], 0
    if (len(_tuple) == 0):
        _tuple = 0, 0
    return _tuple


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = insert_zeros(tuple_a)
    tuple_b = insert_zeros(tuple_b)
    result = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return result
