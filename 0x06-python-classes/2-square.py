#!/usr/bin/python3
"""
A class that defines a square using size and instantiating with the size
@author: Joel Inyang
"""
class Square:
    """
    It defines a square with size after initializing then exceptions are raised for otherwise actions
    """
    def __init__(self, size=0):
        """
        The __init__ function is the constructor function initializing size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
