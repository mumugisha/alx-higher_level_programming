#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    man = []

    for i in matrix:
        y = list(map(lambda x: x * x, i))
        man.append(y)
    
    return man
