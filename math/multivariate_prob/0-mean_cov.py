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
    n, d = X.shape
    if n < 2:
        print("X must contain multiple data points")
    length_of_sums = len(X[0])
    sums = [0] * length_of_sums
    for row in range(len(X)):
        for cell in range(len(X[row])):
            sums[cell] = sums[cell] + X[row, cell]
    means = [x / len(X) for x in sums]
    rounded_means = [[round(x, 8) for x in means]]
    result_means = np.array(rounded_means)

    mean = np.mean(X, axis=0, keepdims=np.True_)

    X_centered = X - mean

    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    # for attribute in X:
    #     mean = np.sum(attribute)
    #     means.append(mean)
    cov = 2
    return result_means, cov
