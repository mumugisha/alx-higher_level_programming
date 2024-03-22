#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    man = []

    for y in matrix:
        y = list(map(lambda x: x * x, y))
        man.append(y)
    
    return man
