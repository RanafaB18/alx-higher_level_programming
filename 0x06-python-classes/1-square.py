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
        self.__size = size
