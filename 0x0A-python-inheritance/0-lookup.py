#!/usr/bin/python3
"""
A method for getting list of attributes
author: Joel Inyang
"""


def lookup(obj):
    """
    Returns the list of available attributes and method
    """
    return dir(obj)
