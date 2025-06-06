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
        Args:
            style_image: the image used as a style reference,
            stored as a numpy.ndarray
            content_image: the imaged used as a content reference,
            stored as a numpy.ndarray
            alpha: the weight for the content cost
            beta: the weight for the style cost
        """
        if (
            not isinstance(style_image, np.ndarray)
            or len(style_image.shape) != 3
            or style_image.shape[2] != 3
        ):
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        if (
            not isinstance(content_image, np.ndarray)
            or len(content_image.shape) != 3
            or content_image.shape[2] != 3
        ):
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        if (type(alpha) is not float and type(alpha) is not int) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")

        if (type(beta) is not float and type(beta) is not int) or beta < 0:
            raise TypeError("beta must be a non-negative number")
        tf.enable_eager_execution()

        self.content_image = self.scale_image(content_image)
        self.style_image = self.scale_image(style_image)
        self.beta = beta
        self.alpha = alpha

    @staticmethod
    def scale_image(image):
        """
        Method that rescales an image such that its
        pixels values are between 0 and 1
        and its largest side is 512 pixels

        Arg:
            image: a numpy.ndarray of shape (h, w, 3)

        returns:
            the scaled image
        """
        if not isinstance(image, np.ndarray) or len(image.shape) != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)"
            )

        h, w, c = image.shape
        if h <= 0 or w <= 0 or c != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)"
            )
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        resized = tf.image.resize_bicubic(
            np.expand_dims(image, axis=0), size=(h_new, w_new)
        )
        rescaled = resized / 255
        rescaled = tf.clip_by_value(rescaled, 0, 1)
        return rescaled

    @staticmethod
    def gram_matrix(input_layer):
        """
        Method that calcuates gram matrices
        args:
            input_layer: tf.Tensor instance or
                tf.variable of shape (1, h, w, c)

        returns:
            tf.Tensor of shape (1, c, c)
        """

        if type(input_layer) is not tf.Tensor or (
            type(input_layer) is not tf.Variable
            or len(input_layer.shape) != 4
            or input_layer.shape[0] != 1
        ):
            raise TypeError("input_layer must be a tensor of rank 4")
