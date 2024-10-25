#!/usr/bin/env python3
"""
Function that perfroms convolutin on grayscale images with custom padding
"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    images, is numpy array, (m,h,w)
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images

    kernel is a numpy arry, (kh, kw)
        kh is the height of the kernel
        kw is the width of the kernel

    padding is a tuple (ph,pw)
        ph is the padding for the height of the image
        pw is the padding for the width of the image
    """

    m, h, w = images.shape
    kh, kw = kernel.shape
    ph = padding[0]
    pw = padding[1]

    padded = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw)), mode="constant"
    )
    convolved_height = h - kh + 2 * ph + 1
    convolved_width = w - kw + 2 * pw + 1
    convolved = np.zeros((m, convolved_height, convolved_width))
    for i in range(convolved_height):
        for j in range(convolved_width):
            box = padded[:, i: i + kh, j: j + kw]
            convolved[:, i, j] = np.sum(box * kernel, axis=(1, 2))

    return convolved
