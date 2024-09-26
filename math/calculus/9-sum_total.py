#!/usr/bin/env python3
"""
Function to Calculate the give intranet summation
"""


def summation_i_squared(n):
    """
    Argument:
    int to be squared as per formula

    Return:
    None if not real integer
    the results' int
    """
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
