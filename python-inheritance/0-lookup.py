#!/usr/bin/python3
"""
Module that defines the function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object

    Returns:
        list: A list
    """
    return (dir(obj))
