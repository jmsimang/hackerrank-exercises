#!/usr/bin/python

"""
CONCATENATE
Two or more arrays can be concatenated together using the concatenate function with
a tuple of the arrays to be joined.

TASK
You are given two integer arrays of size N * P and M * P (N & M are rows, and P is the
column).
Your task is to concatenate the arrays along axis 0.

INPUT FORMAT
The first line contains space separated integers M, N and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

OUTPUT
Print the concatenated array of size (N + M) * P.
"""

import numpy as np
print(np.plyval(np.array(input().split(), dtype=float), int(input())))

