#!/usr/bin/env python3
"""A function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """
    Arguements: A matrix
    Returns: A transpose of that matrix
    """
    transpose = []
    rows = len(matrix)
    cols = len(matrix[0])
    # iterate through the rows
    for i in range(rows):
        row = []
        # iterate through the columns
        for j in range(cols):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose
