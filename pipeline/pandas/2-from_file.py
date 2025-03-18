#!/usr/bin/env python3
"""
Write a function def from_file(filename, delimiter): that loads data from a file as a pd.DataFrame
"""

import pandas as pd

def from_file(filename,delimiter):
    """
    args: filename, delimiter
    returns: the loaded DataFrame
    """

    return pd.read_csb(filename, delimiter=delimiter)

