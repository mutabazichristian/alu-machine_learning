#!/usr/bin/env python3
"""
Function to calculate a correlation matrix
"""
import numpy as np


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

    std_devs = np.sqrt(np.diag(C))

    Co = C / np.outer(std_devs, std_devs)
    return Co
