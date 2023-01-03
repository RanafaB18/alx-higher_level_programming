#!/usr/bin/python3
"""
Adds 2 integers with the add_integer function


"""


def add_integer(a, b=98):
    """Function that adds two integer and/or float numbers

    Args:
        a (int): first integer
        b (int, optional): second integer. Defaults to 98.

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
