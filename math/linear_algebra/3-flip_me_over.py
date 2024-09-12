#!/usr/bin/env python3
"""A method that returns the transpose of a matrix"""


def matrix_transpose(matrix):
    transpose = []
    # loop through the colums
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose
