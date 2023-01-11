#!/usr/bin/python3
"""Defines a function 'save_to_json_file'"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): object
        filename (str): filename
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
