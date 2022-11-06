#!/usr/bin/python3
"""
Class that defines a square using a privste attribute
@author: Joel Inyang
"""
class Square:
    """
    Defines a square with private instance attribute size
    """
    def __init__(self, size):
        """The constructor __init__ method for square class
        Constructor function
        """
        self.__size = size
