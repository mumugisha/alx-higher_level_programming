#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        man = []
    for i in matrix:
	i =list(map(lambda x: x * x, i))
        man.append (i)
    return man
