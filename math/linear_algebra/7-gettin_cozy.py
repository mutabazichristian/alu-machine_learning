#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    # Ensure the matrices can be concatenated
    if axis == 0:
        # Check if the number of columns in both matrices is the same
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Return a new matrix with rows from both matrices
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    elif axis == 1:
        # Check if the number of rows in both matrices is the same
        if len(mat1) != len(mat2):
            return None
        # Concatenate corresponding rows from both matrices
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    # If the axis is not 0 or 1, return None
    return None
