#!/usr/bin/env python3
"""Function that performas a valid convolution on grayscale images"""
import numpy as np
from numpy.core.defchararray import isalnum


def convolve_grayscale_valid(images, kernel):
    """
    Arguments:
    images, a numpy array that contains images to convolve
    kernel, numpy array containing the filter matrix
    """
    a, b = kernel.shape
    if b == a:
        i, m, n = images.shape
        m = m - a + 1
        n = n - b + 1
        convo = np.zeros(m, n)
        for l in range(m):
            for j in range(n):
                convo[l, j] = np.sum(
                    kernel * images[i : i + m, j : j + n]
                )
        convo = np.zeros((i, m, n))
