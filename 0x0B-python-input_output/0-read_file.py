#!/usr/bin/python3
"""Defines the function 'read_file'"""


def read_file(filename=""):
    """Reads from file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line)
