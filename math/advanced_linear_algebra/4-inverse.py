#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""
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
    """Calculate the cofactor matrix."""
    n = len(matrix)
    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def inverse(matrix):
    """
    Calculate the inverse of a given matrix.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: The inverse of the matrix, or None if matrix is singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    det = determinant(matrix)

    if det == 0:
        return None

    if n == 1:
        return [[1 / matrix[0][0]]]

    cofactor_matrix = cofactor(matrix)
    adjugate = list(map(list, zip(*cofactor_matrix)))
    
    inverse_matrix = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
    return inverse_matrix

