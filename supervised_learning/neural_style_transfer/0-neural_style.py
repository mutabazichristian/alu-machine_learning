#!/usr/bin/env python3
"""
Class NSt that pefroms tasks for neural style transfer
"""
import numpy as np
import tensorflow as tf
from tensorflow.image import resize_images


class NST:
    """The Class in question"""

    style_layers = [
        "block1_conv1",
        "block2_conv1",
        "block3_conv1",
        "block4_conv1",
        "block5_conv1",
    ]
    content_layer = "block5_conv2"

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        style_image: image used as style reference,
        content_image: image used as a content reference,
        alpha: the weight of the content cost,
        beta: the weight of style cost
        """
        if (
            not isinstance(style_image, np.ndarray)
            or style_image.ndim != 3
            or style_image.shape[2] != 3
        ):
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")

        if (
            not isinstance(content_image, np.ndarray)
            or content_image.ndim != 3
            or content_image.shape[2] != 3
        ):
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 2)"
            )
        if not isinstance(alpha, int) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, int) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = style_image
        self.content_image = content_image
        self.alpha = alpha
        self.beta = beta

    def scale_image(self, image):
        """
        image: numpy array with shape (h, w, e), with image to be scaled

        returns: scaled image, tf.tensor with shaped (1, h_new, w_new, 3)
        """
        if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
            raise TypeError("image must be a numpy.ndarray with shape(h, w, 3)")

        h, w = image.shape
        if h > w:
            new_h = 512
            new_w = int((w / h * 512))
        else:
            new_w = 512
            new_h = int((h / w) * 512)
        # Convert to float32 and normalize to [0, 1]
        image = image.astype("float32") / 255.0

        # Expand dims to make it (1, h, w, 3)
        image = np.expand_dims(image, axis=0)

        # Use tf.compat.v1 for resizing
        image_tensor = tf.convert_to_tensor(image)
        resized = tf.image.resize_images(
            image_tensor, size=(new_h, new_w), method=tf.image.ResizeMethod.BICUBIC
        )
        return resized
