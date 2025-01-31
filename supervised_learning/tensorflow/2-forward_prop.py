#!/usr/bin/env python3
"""
A function that creates forward propagation throughout our neural network
"""
import tensorflow as tf

create_layer = __import__("1-create_layer").create_layer


def forward_prop(x, layer_sizes, activations):
    """
    args
        x: place holder data
        layer_sizes: a list of number of nodes each layer should have
        activations: a list of activation functions each layer should use
    """
    output = x
    for size, activation in zip(layer_sizes, activations):
        create_layer(output, size, activation)
    return output
