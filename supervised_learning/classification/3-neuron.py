#!/usr/bin/env python3
"""
Class that defines a single neuron performing binary classification
"""
import numpy as np


class Neuron:
    """
    The activation
    """

    def __init__(self, nx):
        """
        The constuctor
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise TypeError("nx must be positive")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """The W property."""
        return self.__W

    @property
    def b(self):
        """The b property."""
        return self.__b

    @property
    def A(self):
        """The A property."""
        return self.__A

    def forward_prop(self, X):
        """
        forward propagation, linear and activation function
        """
        temp = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + exp(-temp))
        return self.__A

    def cost(self, Y, A):
        """
        Cost function that calculates the loss
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        return cost
