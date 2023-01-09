#!/usr/bin/python3
"""Defines the lookup function"""
def lookup(obj):
    """ Returns the list of available attributes and methods of an object

    Args:
        obj (object): instance of some class

    Returns:
        list: list of available attributes and methods of an object:
    """
    return dir(obj)
