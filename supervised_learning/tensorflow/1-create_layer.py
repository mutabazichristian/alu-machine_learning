#!/usr/bin/env python3
"""
A function that creates a layer for our Neural Network
"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """
    arg
        prev: the tensor output of the previous layer
        n: number of nodes in this layer
        activation: the activation function that the layer should use
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=init)
    return layer(prev)
