#!/usr/bin/python3
"""
Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
