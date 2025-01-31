#!/usr/bin/env python3
"""
Write a function that calculates the accuracy of a prediction
"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    args
        y: the actual data
        y_pred: the prediction
    returns
        the accuracy of the predictoin
    """
    return tf.reduce_mean(
        tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1)), tf.float32)
    )
