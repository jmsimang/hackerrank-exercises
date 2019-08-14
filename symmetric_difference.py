#!/usr/bin/python

'''
Task
Given 2 sets of integers, M and N, print their symmetric difference in 
ascending order. The term symmetric difference indicates those values 
that exist in either M or N but do not exist in both.

Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))
R = sorted(M_set.symmetric_difference(N_set))
for i in R:
    print(i)
