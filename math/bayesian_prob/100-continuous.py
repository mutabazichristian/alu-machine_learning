#!/usr/bin/env python3
"""
This module calculates the posterior probability that the probability
of developing severe side effects falls within a specific range.
"""

from scipy import special


def posterior(x, n, p1, p2):
    """
    Calculates the posterior probability that p falls within [p1, p2].

    Args:
        x (int): Number of patients with severe side effects
        n (int): Total number of patients
        p1 (float): Lower bound of the range
        p2 (float): Upper bound of the range

    Returns:
        float: Posterior probability that p is within [p1, p2]
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
    if not isinstance(p1, float) or not 0 <= p1 <= 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or not 0 <= p2 <= 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Calculate the parameters for the Beta distribution
    alpha = x + 1
    beta = n - x + 1

    # Calculate the cumulative probability using the incomplete beta function
    cdf_p2 = special.btdtr(alpha, beta, p2)
    cdf_p1 = special.btdtr(alpha, beta, p1)

    # Calculate the posterior probability
    posterior_prob = cdf_p2 - cdf_p1

    return posterior_prob


if __name__ == "__main__":
    print(posterior(26, 130, 0.17, 0.23))
