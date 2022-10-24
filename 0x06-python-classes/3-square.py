#!/usr/bin/python3

class Square:
    '''Defines a square'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        '''Area of the square'''
        return self._size ** 2
