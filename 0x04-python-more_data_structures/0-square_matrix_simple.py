#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    for row in matrix:
        for x in row:
            return (x ** 2)
