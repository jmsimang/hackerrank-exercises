#!/usr/bin/python

"""
TASK
You are given a set A and N number of other sets. These N number 
of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of 
elements from set A.

CONSTRAINTS
0 < len(set(A)) < 1000
0 < len(otherSets) < 100
0 N < 100

INPUT FORMAT
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2 * N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated 
entries of the operation name and the length of the other set.
The second line of each part contains space separated list of 
elements in the other set.

OUTPUT
Output the sum of elements in set A.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    ins = input().split()
    if ins[0].startswith('int'):
        A.intersection_update(set(map(int, input().split())))
    elif ins[0].startswith('up'):
        A.update(set(map(int, input().split())))
    elif ins[0].startswith('sym'):
        A.symmetric_difference_update(set(map(int, input().split())))
    else:
        A.difference_update(set(map(int, input().split())))
print(sum(A))