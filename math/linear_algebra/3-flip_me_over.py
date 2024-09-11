#!/usr/bin/env python3
"""A function that returns the transpose of a 2D matrix"""
import numpy as np


def matrix_transpose(matrix):
    """
    Arguements: A matrix
    Returns: A transpose of that matrix
    """
    matrix_numpy = np.array(matrix)
    transpose = np.transpose(matrix_numpy)
    return transpose


print(matrix_transpose([[1, 2], [3, 4]]))
print(
    matrix_transpose(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
        ]
    )
)
