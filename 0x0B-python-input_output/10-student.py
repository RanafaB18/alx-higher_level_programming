#!/usr/bin/python3
"""Defines the class 'Student'"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        try:
            if all(type(arg) is str for arg in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        except TypeError:
            pass
        return self.__dict__
