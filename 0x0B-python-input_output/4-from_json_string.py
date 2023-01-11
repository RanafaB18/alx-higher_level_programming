#!/usr/bin/python3
"""Defines the function 'from_json_string'"""
import json


def from_json_string(my_str):
    """Deserializes string to object

    Args:
        my_str (str): String

    Returns:
        object: Deserialized object
    """
    return json.loads(my_str)
