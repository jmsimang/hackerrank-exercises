#!/usr/bin/python

"""
TASK
You are given two arrays A and B. Both have dimensions N x N.
Your task is to compute their matrix product.
INPUT FORMAT
First line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.
OUTPUT
Print the matrix multiplication of A and B.
"""

import numpy as np

N = int(input())
A = np.zeros((N,N), dtype=int)
B = np.zeros((N,N), dtype=int)
for i in range(N):
    A[i] = input().split()
for i in range(N):
    B[i] = input().split()
print(A.dot(B))

