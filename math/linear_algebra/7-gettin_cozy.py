#!/usr/bin/env python3
"""Function that concatenate to matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Arguments: 2 matrices, axis to perfom addition upon
    Returns:
    the concatenated matrix
    None if they can't be concatenated
    """
    if axis == 0:
        return mat1 + mat2
    if axis == 1:
        concat_mat = []
        # check if mat 1 and 2 are the same shape
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat2)):
            mat1[i].append(mat2[i])
        concat_mat = mat1
        return concat_mat
    else:
        return None


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
