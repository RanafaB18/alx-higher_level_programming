#!/usr/bin/python3
"""Defines the function 'to_json_string'"""
import json


def to_json_string(my_obj):
    """Serializes python objects

    Args:
        my_obj (object): object

    Returns:
        str: serialized python object
    """
    return json.dumps(my_obj)
