#!/usr/bin/python3
"""
Module to read and print the content of a file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido, end="")
