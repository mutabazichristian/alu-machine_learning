#!/usr/bin/env python3
"""Function that performs a same convolution on grayscale image"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Arguments:
        images(m,h,w) numpy array:
            m is number of images
            h is height in pixels of images
            w is width in pixels of images
        kernel(kh,kw) numpy array:
            kh is height of the kernel
            kw is width of the kernel
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    ph = (kh - 1) // 2
    pw = (kw - 1) // 2

    padded = np.pad(images, ((0, 0), (ph, pw)), mode="constant")

    convolved = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            box = padded[:, i : i + kh, j : j + kw]
            convolved[:, i, j] = np.sum(box * kernel, axis=(1, 2))
