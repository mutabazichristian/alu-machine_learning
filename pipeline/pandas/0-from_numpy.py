#!/usr/bin/python3 env
"""
A function that creates a pandas data frame from a numpy array
"""
import numpy as np
import pandas as pd

def from_numpy(array):
    return pd.DataFrame(array) 
