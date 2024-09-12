#!/usr/bin/env python3
"""Function that performs addition of elements of 2 arrays"""


def add_arrays(arr1, arr2):
    """
    Arguments: 2 arrays
    Returns: A new array
    """
    if len(arr1) != len(arr2):
        return None
    arr_sum = []
    for i in range(len(arr2)):
        arr_sum.append(arr1[i] + arr2[i])
    return arr_sum


print(add_arrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
