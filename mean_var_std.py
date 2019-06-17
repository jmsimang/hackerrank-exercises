#!/usr/bin/python

"""
TASK
Given a 2-D array with dimensions N x M, your task is to find:
    1. The mean along axis 1
    2. The var along axis 0
    3. The std along axis None
INPUT FORMAT
First line contains the space separated values of N and M.
The next N lines contains M space separated integers.
OUTPUT
First, print the mean.
Second, print the var.
Third, print the std
"""

import numpy as np
np.set_printoptions(legacy='1.13')

N, M = input().split()
arr = np.zeros((int(N), int(M)), dtype=int)
for i in range(int(N)):
    arr[i] = input().split()
print(np.mean(arr, axis=1, np.var(arr, axis=0), np.std(arr, axis=None), sep='\n')

