#!/usr/bin/python3
"""
A filethat creates an Object from  JSON file
@author: Joel Inyang
"""


import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
