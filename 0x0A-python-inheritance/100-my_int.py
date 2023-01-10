#!/usr/bin/python3
"""Defines the class MyInt"""


class MyInt(int):
    """Inverts the return value of
     __eq__ and __ne__ magic methods"""

    def __eq__(self, x):
        """Override == operator"""
        return not super().__eq__(x)

    def __ne__(self, x):
        """Override != operator"""
        return not super().__ne__(x)
