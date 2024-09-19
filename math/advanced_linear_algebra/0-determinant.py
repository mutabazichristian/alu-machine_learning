#!/usr/bin/env python3
"""Function that calculcates the determinant of a matrix"""


def determinant(matrix):
    """
    Args:
    a matrix

    Returns:
    determinant of the matrix
    """

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len((matrix))):
        det += ((-1) ** c) * matrix[0][c] * determinant(minor(matrix, 0, c))
    return det


def minor(matrix, i, j):
    return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]
