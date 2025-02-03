#!/usr/bin/python3
"""
This function returns the list of available attributes and methods
"""


def lookup(obj):
    obj = dir(obj)
    return (obj)
