#!/usr/bin/python3
    """
    This is add_integer module. Its= is a funtion that adda two integers together.
    """
    def add_integer(a, b=98):

        """ Returns the sum of two no """

        if type(a) is not int:
            raise TypeError('a must be an integer')
        if type(b) is not int:
            raise TypeError('b must be an integer')
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
