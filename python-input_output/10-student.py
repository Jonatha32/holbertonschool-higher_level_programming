#!/usr/bin/python3
"""
Module
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and isinstance(attrs, list):
            return {key: value for key, value
                    in self.__dict__.items()if key in attrs}
        return (self.__dict__)
