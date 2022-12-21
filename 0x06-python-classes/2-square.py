#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Create a square"""

    def __init__(self, size=0) -> None:
        """Setup square

        Args:
            self: object
            size: size of square

        Returns:
            None

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
