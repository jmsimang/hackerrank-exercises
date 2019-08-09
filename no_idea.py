#!/usr/bin/python

"""
TASK
There is an array of n integers. There are also 2 disjoint sets, A 
and B, each containing m integers. You like all the integers in set A
and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i element A, you add 1 to your 
happiness. If i element B, you add -1 to your happiness. 
Otherwise, your happiness does not change. 

CONSTRAINTS
1 <= n <= 10^5
1 <= m <= 10^5
1 <= Any integer in the input <= 10^9

INPUT FORMAT
The first line contains integers n and m separated by a space. 
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.

OUTPUT
Output a single integer, your total happiness.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))

happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -=1

print(happiness)
