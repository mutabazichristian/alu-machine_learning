#!/usr/bin/env python3
"""
Class that defines a single neuron perfoming binary classification
"""
import numpy as np

class Neuron:
    def __init__(self,nx):
        if not nx.isdigit():
            raise TypeError("nx must be an integer")
        if not nx>=1:
            raise ValueError("nx must be a positive number")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0

