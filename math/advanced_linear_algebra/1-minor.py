#!/usr/bin/env python3
"""Function that calculate the minor of a matrix"""


def minor(matrix):
    """
    Args:
    matrix: A square matrix (list of lists)

    Returns:
    The minor of the matrix or raises an error for invalid input
    """

    # Check if the matrix is empty
    if matrix == [[]]:  # Handle empty matrix [[]] as a special case
        return 1

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Handle 1x1 matrix case
    if len(matrix) == 1:
        return matrix[0][0]
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
