#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class Circle
    """

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return (math.pi * (self.radius ** 2))

    def perimeter(self):
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (self.width + self.width + self.height + self.height)


def shape_info(shape):
    """
    Print info
    """

    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
