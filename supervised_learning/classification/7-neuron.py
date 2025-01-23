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
        self.__A = 1 / (1 + np.exp(-temp))
        return self.__A

    def cost(self, Y, A):
        """
        Cost function that calculates the loss
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """
        Evaluation function
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        predictions = np.where(A >= 0.5, 1, 0)
        return predictions, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        gradient descent function
        Arguments:
            X numpy array
            Y numpy array
            A numpy array
            alpha: learning rate
        """
        m = X.shape[1]  # Number of examples
        dZ = A - Y  # Derivative of cost with respect to Z
        dW = np.dot(dZ, X.T) / m  # Gradient of weights
        db = np.sum(dZ) / m  # Gradient of bias
        self.__W -= alpha * dW  # Update weights
        self.__b -= alpha * db  # Update bias

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Args:
            X,Y,iterations,alpha
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for _ in range(iterations):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A, alpha)

        return self.evaluate(X, Y)
