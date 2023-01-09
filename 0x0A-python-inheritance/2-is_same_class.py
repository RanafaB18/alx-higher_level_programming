#!/usr/bin/python3
"""Defines the function "is_same_class" """


def is_same_class(obj, a_class):
    """Determines if obj is an instance of a_class

    Args:
        obj (object): object
        a_class (object): class

    Returns:
        bool: True if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
