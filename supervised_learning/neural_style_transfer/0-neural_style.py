#!/usr/bin/env python3

"""
Class NST that performs tasts for neural style transfer
"""
import numpy as np
import tensorflow as tf


class NST:
    """
    The class in question
    """

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Args:
            style_image: the image used as a style reference, stored as a numpy.ndarray
            content_image: the imaged used as a content reference, stored as a numpy.ndarray
            alpha: the weight for the content cost
            beta: the weight for the style cost
        """
        style_layers = [
            "block1_conv1",
            "block2_conv1",
            "block3_conv1",
            "block4_conv1",
            "block5_conv1",
        ]
        content_layer = "block5_conv2"

        if not isinstance(style_image, np.ndarray) or style_image.shape != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        if not isinstance(content_image, np.ndarray) or style_image.shape != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        if not isinstance(alpha, int) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")

        if not isinstance(beta, int) or beta < 0:
            raise TypeError("alpha must be a non-negative number")

        @staticmethod
        def scale_image(image):
            """ """
