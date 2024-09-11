#!/usr/bin/env python3
"""A function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """
    Arguements: A matrix
    Returns: A transpose of that matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
