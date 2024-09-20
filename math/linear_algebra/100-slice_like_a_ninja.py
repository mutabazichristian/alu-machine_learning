#!/usr/bin/env python3
"""Function that slices a matrix along a given axis"""


def np_slice(matrix, axes={}):
    """
    Arguments:
    A numpy array and axis for slicing

    Returns:
    A sliced numpy array:with expression as target:
        pass
    """
    # Create a list of slice objects, one for each dimension of the matrix
    slices = [slice(None)] * matrix.ndim

    # Update the slices based on the provided axes dictionary
    for axis, slice_info in axes.items():
        slices[axis] = slice(*slice_info)

    # Apply the slices to the matrix
    return matrix[tuple(slices)]
