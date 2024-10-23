#!/usr/bin/env python3
"""
Function that performs a valid convolution on grayscale images
"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Arguments:
        image(m,h,w) is a numpy array:
            m is the number of images
            h is the height in pixels of the images
            w is the width in pixels of the images

        kernel(kh, kw) is a numpy array:
            kh is height of the kernel
            kw is the width of the kernel

    Returns:
        a numpy array containing the convolved images
    """

    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = images.shape[0]
    kw = images.shape[1]

    convolved_height = h - kh + 1
    convolved_width = w - kw + 1
    convolved = np.zeros((convolved_height, convolved_width))

    for i in range(h):
        for j in range(w):
            box = images[:, i : i + kh, j : j + kh]
            convolved[:, i, j] = np.sum(box * kernel, axis=(1, 2))

    return convolved
