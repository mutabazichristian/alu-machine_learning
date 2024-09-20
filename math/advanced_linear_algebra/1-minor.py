#!/usr/bin/env python3
"""Function that calculates the minors of a square matrix"""

def minor(matrix):
    """
    Args:
    matrix: A square matrix (list of lists)

    Returns:
    A matrix of minors or raises an error for invalid input
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("matrix must be a list of lists")
    if not matrix or any(len(row) == 0 for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if n == 1:
        return [[1]]

    minors = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            minor_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            minor_row.append(minor_matrix)
        minors.append(minor_row)

    return minors

# Example usage:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(minor(matrix))
