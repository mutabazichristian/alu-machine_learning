#!/usr/bin/env python3
"""
Python script that creates a DataFrame from a dictionary
"""

dictionary = {
        "First":[0.0,0.5,1.0,1.5]
        "Second":['one','two','three','four']
        }

df = pd.DataFrame(dictionary,index=['A','B','C','D'])
