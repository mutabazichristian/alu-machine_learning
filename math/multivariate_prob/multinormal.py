#!/usr/bin/env python3
"""
This module defines the MultiNormal class for
representing a Multivariate Normal distribution.
"""

import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initialize the MultiNormal distribution.

        Args:
            data (numpy.ndarray): Array of shape (d, n) containing the data set
                n is the number of data points
                d is the number of dimensions in each data point

        Raises:
            TypeError: If data is not a 2D numpy.ndarray
            ValueError: If data contains less than 2 data points
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if data.shape[1] < 2:
            raise ValueError(
                "data must contain multiple data points"
            )

        self.mean = np.mean(data, axis=1, keepdims=True)

        # Calculate covariance matrix without using np.cov
        centered_data = data - self.mean
        self.cov = np.dot(centered_data, centered_data.T) / (
            data.shape[1] - 1
        )

    def pdf(self, x):
        """
        Calculate the PDF at a data point.

        Args:
            x (numpy.ndarray): Array of shape (d, 1) containing the data point

        Returns:
            float: The value of the PDF at x

        Raises:
            TypeError: If x is not a numpy.ndarray
            ValueError: If x is not of shape (d, 1)
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")

        det = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)

        diff = x - self.mean
        exponent = -0.5 * np.dot(np.dot(diff.T, inv_cov), diff)

        coefficient = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(det))

        return float(coefficient * np.exp(exponent))


if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.multivariate_normal(
        [12, 30, 10],
        [[36, -30, 15], [-30, 100, -20], [15, -20, 25]],
        10000,
    ).T
    mn = MultiNormal(data)

    print(mn.mean)
    print(mn.cov)

    x = np.random.multivariate_normal(
        [12, 30, 10],
        [[36, -30, 15], [-30, 100, -20], [15, -20, 25]],
        1,
    ).T
    print(x)
    print(mn.pdf(x))
