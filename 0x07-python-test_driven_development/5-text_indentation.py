#!/usr/bin/python3
"""
    Indents text
"""


def text_indentation(text):
    """indent text

    Args:
        text (str): _description_

    Raises:
        TypeError: _description_
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for word in text.split(" "):
        if "." in word or "?" in word or ":" in word:
            line += word + "\n\n"
        else:
            line += word + " "
    print(line.strip())
