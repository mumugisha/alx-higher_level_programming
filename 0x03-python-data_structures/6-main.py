#!/usr/bin/python3

def print_matrix_integer(matrix):
    if matrix:
        for row in matrix:
            print(" ".join("{:d}".format(num) for num in row))

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer([])
