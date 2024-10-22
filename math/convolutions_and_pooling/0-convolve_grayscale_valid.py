#!/usr/bin/env python3
"""Function that performas a valid convolution on grayscale images"""
import numpy as np


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
        convo = np.zeros((i, m, n))
        for i in range(m):
            for j in range(n):
                boxy = images[:, i : i + m, j : j + n]
                convo[:, i, j] = np.sum(boxy * kernel, axis=(1, 2))
    return convo
