#!/usr/bin/python

""" The NumPy module comes with a number of built-in routines for linear algebra
calculations.
linalg.det - computes the determinant of an array
linalg.eig - computes the eigenvalues and right eigenvectors of a square array
linalg.inv - computes the (multiplicative) inverse of a matrix

TASK
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical
characters, digits, lowercase and uppercase characters.

INPUT FORMAT
A single line containing a string S.

CONSTRAINTS
0 < len(S) < 1000

OUTPUT
In the first line, print True if S has any alphanumeric characters. Otherwise print False.
In the second line, print True if S has any alphabetical characters. Otherwise print False.
In the third line, print True if S has any digits. Otherwise print False.
In the fourth line, print True if S has any lowercase characters. Otherwise print False.
In the fifth line, print True if S has any uppercase characters. Otherwise print False.
"""

if __name__ == '__main__':
    s.input()
line_1 = line_2 = line_3 = line_4 = line_5 = False
for c in s:
    if c.isalnum(): line_1 = True
    if c.isalpha(): line_2 = True
    if c.isdigit(): line_3 = True
    if c.islower(): line_4 = True
    if c.isupper(): line_5 = True
print(line_1, line_2, line_3, line_4, line_5, sep='\n')

