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

    def __init__(self, data=None, lambtha=1.0):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = sum(data) / len(data)
            self.data = data
            self.e = 2.7182818285

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
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        lambtha = self.lambtha
        factorial_k = self.factorial(k)
        exp_neg_lambda = self.e
        pmf_value = (lambtha**k) * exp_neg_lambda / factorial_k

        return round(pmf_value, 10)
