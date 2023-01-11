#!/usr/bin/python3
"""Defines the function 'append_after'"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string """
    with open(filename, 'a+') as file:
        for line in file:
            if search_string in line:
                file.write(new_string)
