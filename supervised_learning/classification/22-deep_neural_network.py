#!/usr/bin/env python3
"""
Deep neural network
"""
import numpy as np


class DeepNeuralNetwork:
    """
    Deep
    """

    def __init__(self, nx, layers):
        """Init DNN: nx input, layers node list"""
        if not isinstance(nx, int) or nx < 1:
            raise ValueError("nx must be a positive int")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a non-empty list")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(1, self.__L + 1):
            size = nx if i == 1 else layers[i - 2]
            self.__weights[f"W{i}"] = np.random.randn(layers[i - 1], size) * np.sqrt(
                2 / size
            )
            self.__weights[f"b{i}"] = np.zeros((layers[i - 1], 1))

    def __sigmoid(self, Z):
        """Sigmoid activation"""
        return 1 / (1 + np.exp(-Z))

    def __sigmoid_derivative(self, A):
        """Sigmoid derivative"""
        return A * (1 - A)

    def forward_prop(self, X):
        """Forward prop"""
        self.__cache["A0"] = X
        for i in range(1, self.__L + 1):
            Z = (
                np.dot(self.__weights[f"W{i}"], self.__cache[f"A{i-1}"])
                + self.__weights[f"b{i}"]
            )
            self.__cache[f"Z{i}"] = Z
            self.__cache[f"A{i}"] = self.__sigmoid(Z)
        return self.__cache[f"A{self.__L}"], self.__cache

    def cost(self, Y, A):
        """Binary cross-entropy loss"""
        m = Y.shape[1]
        return -np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A)) / m

    def evaluate(self, X, Y):
        """Eval DNN"""
        A, _ = self.forward_prop(X)
        pred = np.where(A >= 0.5, 1, 0)
        return pred, self.cost(Y, A)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Train DNN"""
        if not isinstance(iterations, int) or iterations <= 0:
            raise ValueError("iterations must be a positive int")
        if not isinstance(alpha, float) or alpha <= 0:
            raise ValueError("alpha must be a positive float")

        for _ in range(iterations):
            A, cache = self.forward_prop(X)
            m = Y.shape[1]
            dZ = A - Y
            for i in range(self.__L, 0, -1):
                dW = np.dot(dZ, cache[f"A{i-1}"].T) / m
                db = np.sum(dZ, axis=1, keepdims=True) / m
                self.__weights[f"W{i}"] -= alpha * dW
                self.__weights[f"b{i}"] -= alpha * db
                if i > 1:
                    dZ = np.dot(
                        self.__weights[f"W{i}"].T, dZ
                    ) * self.__sigmoid_derivative(cache[f"A{i-1}"])
        return self.forward_prop(X)
