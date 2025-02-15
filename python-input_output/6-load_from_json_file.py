#!/usr/bin/python3
"""
Module
"""
import json


def load_from_json_file(filename):
    """
    write
    """
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
    return (f)
