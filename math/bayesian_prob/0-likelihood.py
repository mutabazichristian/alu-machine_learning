#!/usr/bin/env python3
"""
This module calculates the likelihood of side effects for a cancer drug.
"""

import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of developing severe side effects.

    Args:
        x (int): Number of patients with severe side effects
        n (int): Total number of patients
        P (numpy.ndarray): Hypothetical probabilities of side effects

    Returns:
        numpy.ndarray: Likelihood for each probability in P
    """
    # Check if inputs are valid
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate likelihood using binomial distribution
    combo = np.math.factorial(n) / (np.math.factorial(x) * np.math.factorial(n - x))
    return combo * (P**x) * ((1 - P) ** (n - x))


# Test the function (optional)
if __name__ == "__main__":
    P = np.linspace(0, 1, 11)
    print(likelihood(26, 130, P))
