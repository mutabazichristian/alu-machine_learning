#!/usr/bin/env python3
"""A function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    for i in range(len(matrix)):
        print("hi")
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

