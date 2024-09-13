#!/usr/bin/env python3
"""Function that slices a matrix along specific axes"""
import numpy as np


def np_slice(matrix,axes={}):
    """
    Arguments:
    A numpy array to slice
    
    Returns:
    A sliced numpy array
    """
    sliced = matrix[axes]
    return sliced
