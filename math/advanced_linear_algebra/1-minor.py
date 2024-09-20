#!/usr/bin/env python3
"""Function that calculates the minors of a square matrix"""

def minor(matrix):
    """
    Args:
    matrix: A square matrix (list of lists)

    Returns:
    A matrix of minors or raises an error for invalid input
    """

    # Check if the matrix is empty
    if not matrix or matrix == [[]]:  # Handle empty matrix [[]] as a special case
        return 1

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Handle 1x1 matrix case
    if len(matrix) == 1:
        return [[1]]  # The minor of a 1x1 matrix is usually defined as 1

    minors = []
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix)):
            # Create minor by removing row i and column j
            minor_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            minor_row.append(minor_matrix)
        minors.append(minor_row)

    return minors