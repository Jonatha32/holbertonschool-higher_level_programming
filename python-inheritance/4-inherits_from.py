#!/usr/bin/python3
"""
This module returns True if the object is exactly an instance
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is exactly an instance
    """

    return (isinstance(obj, a_class) and type(obj) is a_class)
