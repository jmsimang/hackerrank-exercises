#!/usr/bin/python

"""
TASK
You are given the shape of the array in the form of space separated integers, each integer
representing the size of different dimensions.
Your task is to print an array of the given shape and integer and integer type using the
tools numpy.zeros and numpy.ones.

INPUT FORMAT
A single line containing the space-separated integers.

OUTPUT
First, print the array using the numpy.zeros tool and then print the array with the 
numpy.ones tool.
"""

import numpy as np

X = tuple(int(i) for i in input().split())
print(np.zeros(X, dtype=int) , np.ones(X, dtype=int) , sep='\n')

