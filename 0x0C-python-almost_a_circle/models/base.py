#!/usr/bin/python3
"""
The class base is a super class
"""


class Base:
    """
    A class which is the super class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor function
        """
        if type(id) is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
