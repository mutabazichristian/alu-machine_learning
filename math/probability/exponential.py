#!/usr/bin/env python3
"""
yessir
acusbd
"""


class Exponential:
    """
    A class that represents an exponential distribution.

    """

    def __init__(self, data=None, lambtha=1.0):
        """
        Initialize the Exponential distribution.

        Args:
            data
            lambtha

        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Calculate the Probability Density Function (PDF) for a given x.

        Args:
            x

        Returns:
            float
        """
        if x < 0:
            return 0
        return self.lambtha * self.e ** (-self.lambtha * x)

    def cdf(self, x):
        """
        Calculate the Cumulative Distribution Function (CDF) for a given x.

        Args:
            x

        Returns:
            float
        """
        if x < 0:
            return 0
        return 1 - self.e ** (-self.lambtha * x)

    @property
    def e(self):
        """Approximation of the mathematical constant e."""
        return 2.7182818285
