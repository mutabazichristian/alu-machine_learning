#!/usr/bin/env python3
""" Function that calculates the cofactor of a matrix"""


def determinant(matrix):
    """
    Args:
    matrix

    Returns:
    determinant
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub_matrix)
    return det

def cofactor(matrix):
    """
    Args:
    matrix

    Returns:
    matrix
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
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor))
        cofactor_matrix.append(cofactor_row)
    
    return cofactor_matrix
