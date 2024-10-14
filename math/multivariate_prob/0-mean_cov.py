#!/usr/bin/env python3
"""A function that calculates the mean and covariance of a dataset"""
import numpy as np


def mean_cov(X):
    """
    Arguments:
    X: 2 dimensional numpy of datapoint
        shape: (n,d)

    Returns: mean
        shape: (1,d)
        cov: shape of (d,d)
    """
    if not (isinstance(X, np.ndarray) and X.ndim == 2):
        raise TypeError("X must be a 2D numpy.ndarray")

    if X.n > 2:
        print("Heelo")
    print(X)
    mean = 1
    cov = 2
    return mean, cov
