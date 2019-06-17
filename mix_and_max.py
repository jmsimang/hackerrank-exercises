#!/usr/bin/python

"""
TASK
Given a 2-D array with dimensions N x M, your task is to perform the min
function over axis 1 and then find the max of that.
INPUT FORMAT
First line contains the space separated values of N and M.
The N lines contains M space separated integers.
OUTPUT
Compute the min along axis 1 and then print the max of the result.
"""

import numpy as np
N, M = input().split()
arr = np.zeros((int(N), int(M)), dtype=int)
for i in range(int(N)):
    arr[i] = input().split()
print(np.max(np.min(arr, axis=1)))

