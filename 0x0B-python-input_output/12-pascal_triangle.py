#!/usr/bin/python3
"""Define integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """Generate the integers in pascal triangle"""
    if n <= 0:
        return []
    pascal = []
    for v in range(n):
        temp = []
        for w in range(n):
            temp.append(0)
        pascal.append(temp)
    for v in range(1, n + 1):
        for w in range(v):
            if w == 0:
                pascal[v - 1][w] = 1
            else:
                pascal[v - 1][w] = pascal[v - 2][w] + pascal[v - 2][w - 1]
    formats = []
    for rowe in range(1, n + 1):
        temp = []
        for cols in range(rowe):
            temp.append(pascal[rowe - 1][cols])
        formats.append(temp)
    return formats
