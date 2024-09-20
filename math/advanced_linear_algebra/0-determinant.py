#!/usr/bin/env python3
"""Function that calculcates the determinant of a matrix"""


def determinant(matrix):
    """
    Args:
    a matrix

    Returns:
    determinant of the matrix
    """
    try:
        if not (isinstance(matrix, list) and isinstance(matrix[0], list)):
            return "matrix should be a list"
    except Exception as e:
        return "matrix should be a list"
    if len(matrix) != len(matrix[0]):
        return "matrix should be a square matrix"
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len((matrix))):
        det += ((-1) ** c) * matrix[0][c] * determinant(minor(matrix, 0, c))
    return det


def minor(matrix, i, j):
    return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]


mat0 = [[]]
mat1 = [[5]]
mat2 = [[1, 2], [3, 4]]
mat3 = [[1, 1], [1, 1]]
mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
mat5 = []
mat6 = [[1, 2, 3], [4, 5, 6]]
print(determinant(mat0))
print(determinant(mat1))
print(determinant(mat2))
print(determinant(mat3))
print(determinant(mat4))
try:
    determinant(mat5)
except Exception as e:
    print(e)
try:
    determinant(mat6)
except Exception as e:
    print(e)
