#!/usr/bin/python3
"""
The class base is a super class
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.nb_objects
