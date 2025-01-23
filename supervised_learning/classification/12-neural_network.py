#!/usr/bin/env python3
"""
Class that defines NeuralNetwork
"""
import numpy as np


class NeuralNetwork:
    """
    The class
    """

    def __init__(self, nx, nodes):
        """
        Inits the network
        nx: number of inputs
        nodes: number of nodes in hidden layer
        """
        self.__nx = nx
        self.__nodes = nodes
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = np.zeros((1, 1))
        self.__A1 = None
        self.__A2 = None

    def sigmoid(self, z):
        """Sigmoid activaton function"""
        return 1 / (1 + np.exp(-z))

    def forward_prop(self, X):
        """
        Perform forward propagation
        X: input data
        """
        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = self.sigmoid(Z1)
        Z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = self.sigmoid(Z2)
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Cost function to calculate logisitic loss
        Y: true labels
        A: predicted output
        """
        m = Y.shape[1]
        cost = (-1 / m) * np.sum(
            Y * np.log(A + 1e-10) + (1 - Y) * np.log(1.0000001 - A)
        )
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the model's predictions
        X: input data
        Y: true labels
        """
        A1, A2 = self.forward_prop(X)
        prediction = (A2 >= 0.5).astype(int)
        cost = self.cost(Y, A2)
        return prediction, cost
