#!/usr/bin/env python3
"""Function that slices a matrix along specific axes"""
import numpy as np


def np_slice(matrix, axes={}):
    """
    Arguments:
    A numpy array to slice

    Returns:
    A sliced numpy array
    """
    sliced_objects = [slice(None)] * matrix.dim

    for axis, slice_tuple in axes.items():
        sliced_objects[axis] = slice(*slice_tuple)

    return matrix[tuple(sliced_objects)]
