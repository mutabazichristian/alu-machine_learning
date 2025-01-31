#!/usr/bin/env python3
"""
A function that calculates teh softmax cross-entropy loss of a prediction
"""
import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    args
        y: placeholder for the labes of the input data
        y_pred: a tensor containing the network's prediction
    """
    return tf.losses.softmax_cross_entropy(y, y_pred)
