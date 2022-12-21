#!/usr/bin/python3
"""A Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size) -> None:
        """Setup Square

        Args:
            self: object
            size: size of square

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """size getter

        Args:
            self: object

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Args:
            self: object
            value: value for size

        Returns:
            new value for size
        """
        self.__size = value
