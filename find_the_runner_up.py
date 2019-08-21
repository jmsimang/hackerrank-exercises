#!/usr/bin/python

'''
PROBLEM
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.

INPUT FORMAT
The first line contains n. The second line contains an array of A() of n 
integers each separated by a space.

CONSTRAINTS
2 <= n <= 10
-100 <= A(i) <= 100

OUTPUT FORMAT
Print the runner-up score.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(set(arr)))
    print(arr[len(arr)-2])

