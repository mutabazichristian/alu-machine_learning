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
        
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

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

    def forward_prop(self, X):
        """
        Perform forward propagation.

        Args:
            X (numpy.ndarray): Input data with shape (nx, m).
        Returns:
            numpy.ndarray: The activated output (predictions).
        """
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))  # Sigmoid activation
        return self.__A

    def cost(self, Y, A):
        """
        Calculate the cost using logistic regression.

        Args:
            Y (numpy.ndarray): Correct labels with shape (1, m).
            A (numpy.ndarray): Activated output with shape (1, m).
        Returns:
            float: The logistic regression cost.
        """
        m = Y.shape[1]  # Number of examples
        cost = -(1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Perform one pass of gradient descent.

        Args:
            X (numpy.ndarray): Input data with shape (nx, m).
            Y (numpy.ndarray): Correct labels with shape (1, m).
            A (numpy.ndarray): Activated output with shape (1, m).
            alpha (float): Learning rate.
        Updates:
            __W: Weights after one pass of gradient descent.
            __b: Bias after one pass of gradient descent.
        """
        m = X.shape[1]  # Number of examples
        dz = A - Y
        dW = (1 / m) * np.dot(dz, X.T)
        db = (1 / m) * np.sum(dz)

        # Update weights and bias
        self.__W -= alpha * dW
        self.__b -= alpha * db
