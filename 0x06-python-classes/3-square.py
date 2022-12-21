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

        Raises:
            TypeError: If size isn't an int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size * self.__size
