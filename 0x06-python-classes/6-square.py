#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Create a square"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """Setup square

        Args:
            self: object
            size: size of square

        Returns:
            None
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter function

        Args:
            self: object

        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter function

        Args:
            self: object
            value: new value for size

        Returns:
            None


        Raises:
            TypeError: If size isn't an int
        """
        if not isinstance(value, tuple) or \
            not isinstance(value[0], int) or \
                not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of the square

        Args:
            self: object

        Returns:
            size squared
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square

        Args:
            self: object

        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()
