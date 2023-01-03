#!/usr/bin/python3
"""
    Prints a square
"""


def print_square(size):
    """prints a square of size size

    Args:
        size (int): _description_

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
