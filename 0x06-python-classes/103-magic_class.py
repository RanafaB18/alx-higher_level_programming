#!/usr/bin/python3
"""Assembly"""
import math


class MagicClass:
    """Assemble disassembled code"""

    def __init__(self, radius=0):
        """ setup MagicClass

        Args:
        self: object
            radius:radius

        Returns:
            None
         """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculate area

        Args:
        self: object

        Returns:
            area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculate circumference

        Args:
            self:object

        Returns:
            circumference
        """
        return 2 * math.pi * self.__radius
