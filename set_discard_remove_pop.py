#!/usr/bin/python

"""
PROBLEM
If we want to add a single element to an existing set, we can use 
the .add() operation. 
It adds the element to the set and returns 'None'.

TASK
You have a non-empty set s, and you have to execute 
N commands given in N lines.
The commands will be pop, remove and discard.

CONSTRAINTS
0 < n < 20
0 < N < 20

INPUT FORMAT
The first line contains integer n, the number of elements in the set s. 
The second line contains n space separated elements of set s. 
All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, 
remove and/or discard commands followed by their associated value.

OUTPUT
Print the sum of the elements of set s on a single line.

"""

n = int(input())
s = set(map(int, input().split()))
run = int(input())
for i in range(run):
    ins = input().split()
    if len(ins) == 1:
        s.pop()
    else:
        if ins[0] == 'remove':
            s.remove(int(ins[1]))
        elif ins[0] == 'discard':
            s.discard(int(ins[1]))
print(sum(s))