#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 0 and b == 0:
        return ()
    if a >= 2:
        if b >= 2:
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif b == 1:
            return (tuple_a[0] + tuple_b[0], tuple_a[1])
        elif b == 0:
            return (tuple_a[0], tuple_a[1])
        elif a == 1:
            return (tuple_a[0] + tuple_b[0], tuple_b[1])
        elif a == 0:
            return (tuple_b[0], tuple_b[1])
        else:
            return tuple_a + tuple_b
