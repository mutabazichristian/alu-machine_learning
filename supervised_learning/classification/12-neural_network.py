#!/usr/bin/env python3
"""
Class that defines a neural network with one hidden layer
"""
import numpy as np


class NeuralNetwork:
    """
    Defines a neural network with one
    hidden layer for binary classification.
    """

    def __init__(self, nx, nodes):
        """
        Class constructor.
        Args:
            nx: Number of input features.
            nodes: Number of nodes in the hidden layer.
        Raises:
            TypeError: If nx or nodes is not an integer.
            ValueError: If nx or nodes is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = None
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = np.zeros((1, 1))
        self.__A2 = None
        self.__nx = nx
        self.__nodes = nodes

    def sigmoid(self, z):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-z))

    def forward_prop(self, X):
        """
        Calculate the forward propagation of the neural network
        """
        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = self.sigmoid(Z1)

        Z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = self.sigmoid(Z2)

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Cost funciton
        """
        m = Y.shape[1]
        cost = -np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A))) / m
        return cost

    def evaluate(self, X, Y):
        """
        public method that returns the neuron's preditcion and
        cost of the network,respectively
        """
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        preditcion = np.where(A2 >= 0.5, 1, 0)
        return preditcion, cost

    @property
    def W1(self):
        """The W1 property."""
        return self.__W1

    @property
    def b1(self):
        """The b1 property."""
        return self.__b1

    @property
    def A1(self):
        """The A1 property."""
        return self.__A1

    @property
    def W2(self):
        """The W2 property."""
        return self.__W2

    @property
    def b2(self):
        """The W2 property."""
        return self.__b2

    @property
    def A2(self):
        """The A2 property."""
        return self.__A2
