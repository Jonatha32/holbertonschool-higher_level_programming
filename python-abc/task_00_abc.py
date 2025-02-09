#!/usr/bin/python3
"""
This module is about abstract class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    New class Animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return ("Bark")


class Cat(Animal):
    def sound(self):
        return ("Meow")
