#!/usr/bin/python3
"""This module define a Square class"""


class Square:
    """Represent a Square

        Attributes:
        _size (int): Size of the square
        """
    def __init__(self, size=0):
        """Initializes an instance of Square.

        Args:
        size (int, optional): Size of the square.
            It must be a non -negative integer. By default is 0.

        Raises:
            TypeError: if 'size' is not an integer.
            ValueError: if 'size' is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
