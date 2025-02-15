#!/usr/bin/python3
"""Add al arguments"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# name of the file
filename = "add_item.json"

# try to charge the file list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# add the arguments to the list
items.extend(sys.arg[1:])

# save the updated list in the file
save_to_json_file(items, filename)
