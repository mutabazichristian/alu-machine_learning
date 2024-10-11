#!/usr/bin/env python3
"""
Task 0:
Create a class Poisson
"""


class Poisson:
    """
    Attributes:
    Data
    Lambtha
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
            self.data = data

    def exp(self, x):
        """
        Calculates the exponent of x using expansion
        """

        result = 1.0
        term = 1.0
        for i in range(1, 55):
            term *= x / i
            result += term

        return result

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def pmf(self, k):
        """
        Function that returns the pmf of a given
        Arguments:
        k
        """
        data = self.data
        if not isinstance(k, int):
            k = int(k)
        if k > len(self.data):
            return 0
        lambtha = self.lambtha
        ex = self.exp(-lambtha)
        k_fac = self.factorial(k)
        pmf = (lambtha**k) * ex / k_fac
        return pmf
