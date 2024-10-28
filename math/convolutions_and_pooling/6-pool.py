#!/usr/bin/env python3
"""Module for pooling operation on images"""

import numpy as np


def pool(images, kernel_shape, stride, mode="max"):
    """
    Performs pooling on images.

    Args:
        images (numpy.ndarray): Array of shape (m, h, w, c) containing multiple images
        kernel_shape (tuple): Tuple of (kh, kw) containing the kernel shape for pooling
        stride (tuple): Tuple of (sh, sw) containing stride values
        mode (str): Type of pooling ('max' or 'avg')

    Returns:
        numpy.ndarray: Array containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # Calculate output dimensions
    out_h = (h - kh) // sh + 1
    out_w = (w - kw) // sw + 1

    # Initialize output array
    output = np.zeros((m, out_h, out_w, c))

    # Perform pooling
    for i in range(out_h):
        for j in range(out_w):
            if mode == "max":
                output[:, i, j, :] = np.max(
                    images[
                        :,
                        i * sh : i * sh + kh,
                        j * sw : j * sw + kw,
                        :,
                    ],
                    axis=(1, 2),
                )
            elif mode == "avg":
                output[:, i, j, :] = np.mean(
                    images[
                        :,
                        i * sh : i * sh + kh,
                        j * sw : j * sw + kw,
                        :,
                    ],
                    axis=(1, 2),
                )

    return output
