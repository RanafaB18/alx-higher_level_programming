#!/usr/bin/python3
""" Defines a class "MyList" """


class MyList(list):
    """Replica of the list datatype"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
