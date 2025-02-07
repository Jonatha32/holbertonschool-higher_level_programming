#!/usr/bin/python3
"""
Create a new class called Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    New class
    """

    def __init__(self, size):
        """
        Init
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area
        """
        return (self.__size * self.__size)
