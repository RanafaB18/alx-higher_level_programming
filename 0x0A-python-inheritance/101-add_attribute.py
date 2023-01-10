#!/usr/bin/python3
"""Defines the add_attribute function"""


def add_attribute(obj, key, value):
    """Adds new attribute to obj if possible

    Args:
        obj (object): object
        key (str): key
        value (any): value

    Raises:
        TypeError: if it can't add a new attribute
    """
    types = [
        int,
        float,
        complex,
        bool,
        str,
        bytes,
        bytearray,
        list,
        tuple,
        range,
        set,
        frozenset,
        dict,
        None
    ]
    for kind in types:
        if type(obj) == kind:
            raise TypeError("can't add new attribute")
    setattr(obj, key, value)
