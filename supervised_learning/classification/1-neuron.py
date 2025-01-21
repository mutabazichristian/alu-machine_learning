#!/usr/bin/env python3
"""Module that defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """
    Class that defines a single neuron
    """

    def __init__(self, nx):
        """
        Constructor function
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """The A property."""
        return self.__W

    @property
    def b(self):
        """The b property."""
        return self.__b

    @property
    def A(self):
        """The A property."""
        return self.__A
