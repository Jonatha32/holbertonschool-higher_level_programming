#!/usr/bin/python3
"""
Module
"""


def append_write(filename="", text=""):
    """
    Write
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
