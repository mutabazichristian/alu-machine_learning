#!/usr/bin/env python3
"""A function that add 2 matricess together"""


def add_matrices2D(mat1, mat2):
    """
    arguments: 2 matrices
    returns: the addition matrix of the 2 matrices
    """
    sum_mat = []
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2)):
        return None
    # loop through row
    for i in range(len(mat2)):
        row = []
        for j in range(len(mat2[0])):
            row.append(mat1[i][j] + mat2[i][j])
        sum_mat.append(row)
    return sum_mat


print(add_matrices2D([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
