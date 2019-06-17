#!/usr/bin/python

""" The NumPy module comes with a number of built-in routines for linear algebra
calculations.
linalg.det - computes the determinant of an array
linalg.eig - computes the eigenvalues and right eigenvectors of a square array
linalg.inv - computes the (multiplicative) inverse of a matrix

TASK
You are given a square matrix A with dimensions N * N.
Your task is to find the determinant.

INPUT FORMAT
The first line contains the integer N.
The next N lines contains the N space separated elements of array A.

OUTPUT
Print the determinant of A (rounded to 2 decimal places).
"""

import numpy as np

N = int(input())
A = np.zeros((N, N), dtype=float)
for i in range(N):
    A[i] = input().split()
print(np.round(np.linalg.det(A), 2))

