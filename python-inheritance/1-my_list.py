#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that provides an adittional method to print
    the elements of the list.
    """

    def print_sorted(self):
        """
        Prints the elements
        """

        print(sorted(self))
