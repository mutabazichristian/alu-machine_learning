#!/usr/bin/env python3
"""
cnaiurwedsncj
"""


class Normal:
    """
    A class that represents a normal distribution.
    """

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        """
        Initialize the Normal distribution.

        Args:
            data
            mean
            stddev

        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5

    def z_score(self, x):
        """Calculate the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the Probability Density Function"""
        coefficient = 1 / (self.stddev * (2 * self.pi) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * self.e**exponent

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        Args:
            x: the x-value
        """
        z = (x - self.mean) / (self.stddev * (2**0.5))
        return 0.5 * (1 + self.erf(z))

    def erf(self, x):
        """
        Calculate the error function.
        """
        if abs(x) >= 2.5:
            return 1.0 if x >= 0 else -1.0
        a = 0.140012
        t = 1 / (1 + a * abs(x))
        erf = 1 - t * self.e ** (
            -x * x
            - 1.26551223
            + 1.00002368 * t
            + 0.37409196 * t**2
            + 0.09678418 * t**3
            - 0.18628806 * t**4
            + 0.27886807 * t**5
            - 1.13520398 * t**6
            + 1.48851587 * t**7
            - 0.82215223 * t**8
            + 0.17087277 * t**9
        )
        return erf if x >= 0 else -erf

    @property
    def pi(self):
        """Approximation of pi."""
        return 3.1415926535897932

    @property
    def e(self):
        """Approximation of e."""
        return 2.7182818284590452
