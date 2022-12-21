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

        self.size = size

    @property
    def size(self):
        """size getter function

        Args:
            self: object

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter function

        Args:
            self: object
            value: new value for size

        Returns:
            None


        Raises:
            TypeError: If size isn't an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of the square

        Args:
            self: object

        Returns:
            size squared
        """
        return self.__size * self.__size
