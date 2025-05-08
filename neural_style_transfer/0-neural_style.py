#!/usr/bin/env python3
"""
Class NSt that pefroms tasks for neural style transfer
"""

import numpy as np

class NST:
    """The Class in question"""

    style_layers = ['block1_conv1','block2_conv1','block3_conv1','block4_conv1','block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
            style_image: image used as style reference,
            content_image: image used as a content reference,
            alpha: the weight of the content cost,
            beta: the weight of style cost
        """
        if not isinstance(style_image,np.ndarray) or style_image.ndim != 3 or style_image.shape[2] !=3:
            raise TypeError('style_image must be a numpy.ndarray with shape (h, w, 3)')

        if not isinstance(content_image, np.ndarray) or content_image.ndim !=3 or content_image.shape[2] !=3:
            raise TypeError('content_image must be a numpy.ndarray with shape (h, w, 2)')
        if not isinstance(alpha, int) or alpha<0:
            raise TypeError('alpha must be a non-negative number')
        if not isinstance(beta, int) or beta<0:
            raise TypeError('beta must be a non-negative number')

        self.style_image = style_image
        self.content_image = content_image
        self.alpha = alpha
        self.beta = beta

    def scale_image(image):
        """
        image: numpy array with shape (h, w, e), with image to be scaled

        returns: scaled image, tf.tensor with shaped (1, h_new, w_new, 3)
        """
        if not isinstance(image, np.ndarray) or image.ndim !=3 or image.shape[2] != 3:
            raise TypeError('image must be a numpy.ndarray with shape(h, w, 3)')
