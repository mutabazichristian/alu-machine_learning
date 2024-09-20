#!/usr/bin/env python3
"""Function that calculates the minor of a matrix"""


def minor(matrix, i, j):
    """
    Args:
    matrix: A square matrix (list of lists)
    i: The row index of the element to find the minor for
    j: The column index of the element to find the minor for

    Returns:
    The minor of the matrix element at (i, j)
    or raises an error for invalid input
    """

    # Check if the matrix is empty
    # Handle empty matrix [[]] as a special case
    if not matrix or matrix == [[]]:
        return 1

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Handle 1x1 matrix case
    if len(matrix) == 1:
        return matrix[0][0]

    # Create minor by removing row i and column j
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

# Example usage:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(minor(matrix, 1, 1))  # Should return [[1, 3], [7, 9]]
