#!/usr/bin/python

"""
TASK
Your task is to print an array of size N * M with its main diagnal elements 
as 1's and 0's everywhere else.

INPUT FORMAT
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

OUTPUT
Print the desired N * M array.
"""

import numpy as np
np.set_printoptions(legacy='1.13')

x, y = input().split()
print(np.eye(int(x), int(y), k=0))

