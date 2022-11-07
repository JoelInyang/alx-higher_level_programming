#!/usr/bin/python3
"""
It is a class that defines a square. It attribute is size
"""

class Square:
    """
    Defines a square with private attribute of size and also defines the area of the square
    """
    def __init__(self, size=0):
        """ __init__ is he constructor functionthat has the size it raises two exceptions (TypeError and ValueError)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of the square is being calculated
        Returns size squared
        """
        return self.__size ** 2
