#!/usr/bin/env python3
"""Module for convolution operation on images with channels"""

import numpy as np


def convolve_channels(images, kernel, padding="same", stride=(1, 1)):
    """
    Performs a convolution on images with channels.

    Args:
        images (numpy.ndarray): Array of shape (m, h, w, c) containing multiple images
        kernel (numpy.ndarray): Array of shape (kh, kw, c) containing the convolution kernel
        padding (tuple or str): Padding type ('same', 'valid') or tuple (ph, pw)
        stride (tuple): Tuple of (sh, sw) containing stride values

    Returns:
        numpy.ndarray: Array containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, _ = kernel.shape
    sh, sw = stride

    # Handle padding
    if padding == "same":
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == "valid":
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad the images
    padded = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), mode="constant"
    )

    # Calculate output dimensions
    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1

    # Initialize output array
    output = np.zeros((m, out_h, out_w))

    # Perform convolution
    for i in range(out_h):
        for j in range(out_w):
            output[:, i, j] = np.sum(
                padded[
                    :, i * sh : i * sh + kh, j * sw : j * sw + kw, :
                ]
                * kernel,
                axis=(1, 2, 3),
            )

    return output