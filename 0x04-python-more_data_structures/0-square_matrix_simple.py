#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for x in row:
                return (x ** 2)
