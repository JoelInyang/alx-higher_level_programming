#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0):
        self.size = size
        self.postion = postion

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
        raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
