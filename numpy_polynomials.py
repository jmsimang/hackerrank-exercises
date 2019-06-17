#!/usr/bin/python

"""
poly - returns the coefficients of a polynomial with a given sequence of roots.
roots - returns the roots of a polynomial with the given coefficients.
polyint - return an antiderivative (indefinite integral) of a polynomial.
polyder - returns the derivative of the specified order of a polynomial.
polyval - evaluates the polynomial at specific value.
polyfit - fits a polynomial of a specified order to a set of data using a 
        least-squares approach.

TASK
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
INPUT FORMAT
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.
OUTPUT
Print the desired value.
"""

import numpy as np
print(np.plyval(np.array(input().split(), dtype=float), int(input())))

