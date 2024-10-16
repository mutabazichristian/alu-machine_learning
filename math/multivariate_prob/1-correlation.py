#!/usr/bin/env python3
"""
Function to calculate a correlation matrix
"""
import numpy as np
from numpy.core import shape


def correlation(C):
    """
    Arguments:
    C, a numpy array
        shape (d,d) where d is the number of dimensions
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if not len(C.shape) == 2:
        raise ValueError("C must be a 2D square matrix")
    a, b = C.shape
    if a != b:
        raise ValueError("C must be a 2D square matrix")
    Co = 1
    return Co
