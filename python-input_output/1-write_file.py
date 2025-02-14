#!/usr/bin/python3
"""
Module
"""


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
