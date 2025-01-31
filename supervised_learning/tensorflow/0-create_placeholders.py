#!/usr/bin/env python3
"""Function that returns two placeholders for the neural network"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Args:
        nx: the number of feauture columns in our data
        classes: the number of classe in our classifier
    Returns:
        x: is the placeholder for the input data to the neural network
        y: is the placeholder for the one-hot lables for the input data
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name="x")
    y = tf.placeholder(tf.float32, shape=(None, classes), name="y")
    return x, y
