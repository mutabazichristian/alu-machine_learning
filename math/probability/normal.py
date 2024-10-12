#!/usr/bin/env python3

"""
Class that represents a normal distribution
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
        Returns:
            The CDF value for x
        """
        z = (x - self.mean) / (self.stddev)
        return (1 + self.erf(z / 2**0.5)) / 2

    def erf(self, x):
        """
        Calculate the error function using a Taylor series approximation.
        """
        # Constants
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911

        # Save the sign of x
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        # A&S formula 7.1.26
        t = 1.0 / (1.0 + p * x)
        y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * self.e ** (
            -x * x
        )

        return sign * y

    @property
    def pi(self):
        """Approximation of pi."""
        return 3.1415926535897932

    @property
    def e(self):
        """Approximation of e."""
        return 2.7182818284590452
