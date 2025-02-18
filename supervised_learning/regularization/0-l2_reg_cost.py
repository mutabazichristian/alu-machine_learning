#!/usr/bin/env python3
"""Function that calculates the cost of a neural network"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    Arguments:
        cost: the cost of the network without L2 regularization
        lambtha: the regularization parameter
        weights: a dictionary of weights and biases(numpy.ndarray) of the neural network
        L: the number of layers in the neural network
        m: number of data points used

    Returns:
        The cost of the network accounting for L2 regularization
    """
    for i in range(1, L+1):
        W = weights['W'+str(i)]
        b = weights['b'+str(i)]
        cost += lambtha/2 * np.sum(np.square(W))
    cost = 1
    return cost
