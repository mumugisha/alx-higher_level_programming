#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared.append([c**2 for c in row])
    return squared
