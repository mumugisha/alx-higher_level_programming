#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for y in matrix:
        y = list(map(lambda x: x * x, y))
        new.append(y)
    return new
