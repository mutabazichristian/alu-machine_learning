#!/usr/bin/env python3
"""Neuron module for binary classification."""

import numpy as np


class Neuron:
    """Defines a single neuron for binary classification."""
    
    def __init__(self, nx):
        """
        Initialize a Neuron instance.

        Args:
            nx (int): The number of input features to the neuron.
        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")
        
        # Private attributes
        self.__W = np.random.randn(1, nx)  # Weights vector
        self.__b = 0  # Bias
        self.__A = 0  # Activated output (prediction)

    @property
    def W(self):
        """Getter for the weights vector."""
        return self.__W

    @property
    def b(self):
        """Getter for the bias."""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output."""
        return self.__A
