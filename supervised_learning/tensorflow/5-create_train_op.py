#!/usr/bin/env python3
"""
Function that creates the training operation for the network
"""
import tensorflow as tf


def create_train_op(loss, alpha):
    """
    args
        loss: the loss of the network's prediction
        alpha: is the learning rate
    """
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
