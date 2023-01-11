#!/usr/bin/python3
"""Defines a function 'append_write'"""


def append_write(filename="", text=""):
    """Appends text to a file

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".

    Returns:
        int: number of characters written to file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
