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

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        gradient_descent
        """
        m = Y.shape[1]
        dz2 = A2 - Y
        dw2 = (1 / m) * np.matmul(dz2, A1.T)
        db2 = (1 / m) * np.sum(dz2, axis=1, keepdims=True)
        dz1 = np.matmul(self.__W2.T, dz2) * (A1 * (1 - A1))
        dw1 = (1 / m) * np.matmul(dz1, X.T)
        db1 = (1 / m) * np.sum(dz1, axis=1, keepdims=True)
        self.__W2 = self.__W2 - (alpha * dw2)
        self.__b2 = self.__b2 - (alpha * db2)
        self.__W1 = self.__W1 - (alpha * dw1)
        self.__b1 = self.__b1 - (alpha * db1)
        return self.__W1, self.__b1, self.__W2, self.__b2

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Train
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")

        if iterations < 1:
            raise ValueError("iterations must be a positive integer")

        if type(alpha) is not float:
            raise TypeError("alpha must be a float")

        if alpha < 0:
            raise ValueError("alpha must be positive")

        if graph or verbose:
            if type(step) is not int:
                raise TypeError("step must be an integer")

            if step < 1 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        costs = []
        iteration_list = []

        for i in range(iterations + 1):
            A1, A2 = self.forward_prop(X)
            cost = self.cost(Y, A2)
            costs.append(cost)
            iteration_list.append(i)

            if verbose and i % step == 0:
                print("Cost after iteration {}: {}".format(i, cost))

            self.gradient_descent(X, Y, A1, A2)

        evaluation = self.evaluate(X, Y)

        if graph:
            plt.plot(iteration_list, costs, "b-")
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()

        return evaluation @ property

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
