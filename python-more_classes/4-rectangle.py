#!/usr/bin/python3
"""This module defines an empty class Rectangle."""


class Rectangle:
    """This class defines a square"""
    def __init__(self, width=0, height=0):
        """Initilizes a new rectangle.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Return:
            The area of rectangle.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Return:
            The perimeter of rectange.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height + self.__width + self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return ("\n".join("#" * self.width for _ in range(self.height)))

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")
