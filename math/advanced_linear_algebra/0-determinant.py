#!/usr/bin/env python3
"""Function that calculates the determinant of a matrix"""


def determinant(matrix):
    """
    Args:
    matrix: A square matrix (list of lists)

    Returns:
    The determinant of the matrix or raises an error for invalid input
    """
    # Check if the input is a list of lists (matrix)
    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix should be a list of lists")

    # Check for empty matrix or inconsistent row lengths
    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Handle special cases
    if len(matrix) == 1:  # 1x1 matrix
        return matrix[0][0]
    if len(matrix) == 2:  # 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for c in range(len(matrix[0])):  # Loop through columns of the first row
        # Calculate the minor matrix for element (0, c)
        minor_matrix = minor(matrix, 0, c)
        # Accumulate the determinant using cofactor expansion
        det += ((-1) ** c) * matrix[0][c] * determinant(minor_matrix)

    return det


def minor(matrix, i, j):
    """Returns the minor of the matrix by removing the ith row and jth column."""
    # Ensure that the minor matrix is properly constructed by skipping the ith row and jth column
    return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]
