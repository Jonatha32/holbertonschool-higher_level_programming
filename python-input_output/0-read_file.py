#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, "r") as f:
        contenido = f.read()
        print(contenido)
