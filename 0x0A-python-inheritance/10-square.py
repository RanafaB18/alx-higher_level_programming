#!/usr/bin/python3
"""Defines the class "Rectangle" """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines the class Square """
    def __init__(self, size):
        """Initialize square object"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
