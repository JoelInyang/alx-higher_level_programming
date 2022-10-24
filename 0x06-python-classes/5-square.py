#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        return self._size ** 2

    def my_print(self):
        if size == 0:
            print(" ")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end=" ")
                print()
