#!/usr/bin/python3
"""
It defines a square with attribute of size and position respectively 
also get the area of the square and print #
"""

class Square:
    """
    A square with all it properties
    """
    def __init__(self, size=0, position=(0, 0):
        """
        The __init__ is the constructor function having size and position as parameters
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        It defines the size of the square and returns the size with the getter attribute
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        It defines the size with the setter atttribute
        """
        if type(value) is not int:
        raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    @property
    def position(self):
        """
        It defines the position of the square and returns the size with the getter attribute
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        It defines the position with the setter atttribute
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        The area returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints # in the form of a square
        """
        if size == 0:
            print( )
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end=" ")
                print()
