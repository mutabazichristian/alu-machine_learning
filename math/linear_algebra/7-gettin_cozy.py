#!/usr/bin/env python3
"""Function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Arguments:
    2 matrices and the specific axis

    Returns:
    The concatenated matrix,
    None, if they can't be conc

    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return None
