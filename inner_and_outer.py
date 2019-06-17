#!/usr/bin/python

"""
TASK
You are given two arrays A and B.
Your task is to compute their inner and outer product.
INPUT FORMAT
The first line contains the space separated integers of array A.
The second line contains the space separated integers of array B.
OUTPUT
First, print the inner product.
Second, print the outer product
"""

import numpy as np

A, B = np.array(input().split(), dtype=int), np.array(input().split(), dtype=int)
print(np.inner(A, B), np.outer(A, B), sep='\n')

