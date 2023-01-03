#!/usr/bin/python3
"""
    Prints a sentence
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: if last_name or first_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
