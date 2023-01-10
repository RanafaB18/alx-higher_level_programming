#!/usr/bin/python3
"""Defines a function "inherits_from" """


def inherits_from(obj, a_class):
    """Checks if the obj is an instance of a_class

    Args:
        obj (object): object
        a_class (object): class

    Returns:
        bool: True if obj is an instance of a class
        that inherited from from a_class else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
