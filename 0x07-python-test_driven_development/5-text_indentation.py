#!/usr/bin/python3
"""
5-text_indentation.py will print blankline after any of these '.', ':', '?'
"""


def text_indentation(text):
    """
    prints new lines after some specific character
    """
    if type(text) is not string:
        raise TypeError('text must be a string')

    string = text.replace('.', '.\n\n').replace
    ('?', '?\n\n').replace(':', ':\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')
    print(string, end="")
