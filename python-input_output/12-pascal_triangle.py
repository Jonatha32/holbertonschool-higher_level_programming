#!/usr/bin/python3
"""
Module
"""


def pascal_triangle(n):
    """
    pascal triangulo
    """
    if n <= 0:
        return []

    triangulo = [[1]]

    for a in range(1, n):
        fila = [1]

        fila_anterior = triangulo[a - 1]

        for b in range(1, a):
            fila.append(fila_anterior[b - 1] + fila_anterior[b])
        fila.append(1)

        triangulo.append(fila)
    return (triangulo)
