#!/usr/bin/env python3
"""A function that calculates the mean and covariance of a dataset"""
from typing import Any
import nump as np

def mean_cov(X):
    """
    Arguments:
    X: 2 dimensional numpy of datapoint
        shape: (n,d)

    Returns: mean
        shape: (1,d)
        cov: shape of (d,d)
    """
    if not (isinstance(X,np.ndarray) and X.ndim == 2):
        raise TypeError('X must be a 2D numpy.ndarray')

    if X.n > 2:
        raise ValueError('X must contain multiple datapoint')
    mean = 1
    cov = 2
    return mean, cov
