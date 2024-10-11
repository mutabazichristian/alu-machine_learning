#!/usr/bin/env python3
import math
"""
Task 0:
Create a class Poisson
"""


class Poisson:
    """
    Attributes:

    """

    def __init__(self, data=None, lambtha=1):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        if not isinstance(k, int):
            k = int(k)
        if k > len(data):
            return 0
        lambtha = self.lambtha
        pmf = (lambtha ** k) * math.exp(-lambtha)/math.factorial(k)
