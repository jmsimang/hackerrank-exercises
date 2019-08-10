#!/usr/bin/python

"""
TASK
You are given two sets of student roll numbers. One set has subscribed 
to the English newspaper, and the other set is subscribed to the 
French newspaper. The same student could be in both sets.
Your task is to find the total number of students who have subscribed 
to at least one newspaper.

CONSTRAINTS
1 <= Total number of students in college < 1000

INPUT FORMAT
The first line contains an integer, n, the number of students who have 
subscribed to the English newspaper. 
The second line contains n space separated roll numbers of those students. 
The third line contains b, the number of students who have subscribed to 
the French newspaper. 
The fourth line contains b space separated roll numbers of those students.

OUTPUT
Output the total number of students who have subscriptions to both 
English and French newspapers.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
e = set(map(int, input().split()))
b = int(input())
print(len(e.intersection(set(map(int, input().split())))))
