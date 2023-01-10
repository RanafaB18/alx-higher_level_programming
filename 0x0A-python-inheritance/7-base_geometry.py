#!/usr/bin/python3
"""Defines the class "BaseGeometry" """


class BaseGeometry:
    """Defines the instance method "area" """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
