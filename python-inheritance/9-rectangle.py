#!/usr/bin/python3
"""
Create a new empty class called BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    New class
    """

    def __init__(self, width, height):
        """
        Init with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Print string
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
