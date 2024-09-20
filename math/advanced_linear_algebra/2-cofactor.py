#!/usr/bin/env python3
""" Function that calculates the cofactor of a matrix"""
import numpy as np


def cofactor(matrix):
    """
    Args:
    matrix: some matrix

    Returns:
    cofactor matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    n = len(matrix)
    
    if n == 1:
        return [[1]]
    
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor_row.append(((-1) ** (i + j)) * int(round(np.linalg.det(minor))))
        cofactor_matrix.append(cofactor_row)
    
    return cofactor_matrix
