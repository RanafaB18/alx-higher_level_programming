#!/usr/bin/python3
""" Defines a class "MyList" """


class MyList(list):
    """Replica of the list datatype"""

    def __init__(self):
        """Initializes the class
        """
        list.__init__(self)

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
