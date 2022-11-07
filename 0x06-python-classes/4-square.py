#!/usr/bin/python3
"""
It defines a class square that has attribute size, a getter and setter is implemented as well.
"""

class Square:
    """
    The class along with the size also defines the area.
    """
    def __init__(self, size=0):
        """
        The __init__ is the constructor function that initializes size
        """
        self.__size = size

    @property
    def size(self):
        """
        It returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        it raises exceptions and also returns the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        It returns the area of the square by raising size to the power of 2
        """
        return self.__size ** 2
