#!/usr/bin/python3
"""Defines the function 'class_to_json'"""
import json


def class_to_json(obj):
    """ returns the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object

    Args:
        obj (object): object

    Returns:
        dict: attributes of the object
    """
    return json.loads((json.dumps(obj.__dict__)))
