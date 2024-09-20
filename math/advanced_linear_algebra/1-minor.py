#!/usr/bin/env python3
"""Function that calculates the minor of a matrix"""
def minor(matrix):
    """
    Args:
    matrix: A square matrix (list of lists)

    Returns:
    The minor of the matrix or raises an error for invalid input
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is empty
    if not matrix:
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Check if all rows have the same length and if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]
    
    # Function to calculate determinant of a sub-matrix
    def determinant(sub_matrix):
        if len(sub_matrix) == 1:
            return sub_matrix[0][0]
        if len(sub_matrix) == 2:
            return sub_matrix[0][0] * sub_matrix[1][1] - sub_matrix[0][1] * sub_matrix[1][0]
        
        det = 0
        for j in range(len(sub_matrix)):
            sub_det = determinant([row[:j] + row[j+1:] for row in sub_matrix[1:]])
            det += ((-1) ** j) * sub_matrix[0][j] * sub_det
        return det
    
    # Calculate minor matrix
    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create sub-matrix by removing i-th row and j-th column
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            minor_row.append(determinant(sub_matrix))
        minor_matrix.append(minor_row)
    
    return minor_matrix