#!/usr/bin/env python3
"""
This module calculates the marginal probability of obtaining the data.
"""

import numpy as np


def marginal(x, n, P, Pr):
    """
    Calculates the marginal probability of obtaining the data.

    Args:
        x (int): Number of patients with severe side effects
        n (int): Total number of patients
        P (numpy.ndarray): Hypothetical probabilities of side effects
        Pr (numpy.ndarray): Prior beliefs of P

    Returns:
        float: Marginal probability of obtaining x and n
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
        )
    if np.any((P < 0) | (P > 1)):
        raise ValueError(
            "All values in P must be in the range [0, 1]"
        )
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError(
            "All values in Pr must be in the range [0, 1]"
        )
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate likelihood
    combo = np.math.factorial(n) / (
        np.math.factorial(x) * np.math.factorial(n - x)
    )
    likelihood = combo * (P**x) * ((1 - P) ** (n - x))

    # Calculate marginal probability
    return np.sum(likelihood * Pr)


# Test the function (optional)
if __name__ == "__main__":
    P = np.linspace(0, 1, 11)
    Pr = np.ones(11) / 11
    print(marginal(26, 130, P, Pr))
