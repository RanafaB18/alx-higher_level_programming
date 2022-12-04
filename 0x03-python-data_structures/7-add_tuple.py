#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) == 1:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    else:
        return tuple_a + tuple_b
