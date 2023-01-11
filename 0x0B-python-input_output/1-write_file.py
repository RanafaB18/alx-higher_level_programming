#!/usr/bin/python3
"""Defines a function 'write_file'"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".

    Returns:
        int: number of characters written to file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
