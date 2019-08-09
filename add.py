#!/usr/bin/python

"""
PROBLEM
If we want to add a single element to an existing set, we can use 
the .add() operation. 
It adds the element to the set and returns 'None'.

TASK
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the 
total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a 
stack of N country stamps.

Find the total number of distinct country stamps.

CONSTRAINTS
0 < N < 1000

INPUT FORMAT
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

OUTPUT
Output the total number of distinct country stamps on a single line.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
s = len(set([input() for i in range(N)]))
print(s)
