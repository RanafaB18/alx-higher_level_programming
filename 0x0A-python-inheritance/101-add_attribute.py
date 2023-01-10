#!/usr/bin/python3
"""Defines the add_attribute function"""
import builtins


def add_attribute(obj, key, value):
    """Adds new attribute to obj if possible

    Args:
        obj (object): object
        key (str): key
        value (any): value

    Raises:
        TypeError: if it can't add a new attribute
    """
    if type(obj) in builtins.__dict__.values():
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
