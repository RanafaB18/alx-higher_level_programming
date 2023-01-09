#!/usr/bin/python3
"""Defines a function "is_kind_of_class" """


def is_kind_of_class(obj, a_class):
    """Checks if the obj is an instance of a_class

    Args:
        obj (object): object
        a_class (object): class

    Returns:
        bool: True if obj is an instance of a_class else False
    """
    return isinstance(obj, a_class)
