"""
PROBLEM
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in 
combination. Together, they form an iterator algebra making it possible to construct specialized tools 
succinctly and efficiently in pure Python.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices 
(assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

INPUT FORMAT
The input consists of three lines. The first line contains the integer N, denoting the length of the list. 
The next line consists of space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

OUTPUT FORMAT
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:''.
Note: The answer must be correct up to 3 decimal places.

CONSTRAINTS
1 <= N <= 10
1 <= K <= N
All the letters in the list are lowercase English letters.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

N = int(input())
letters = input().split()
K = int(input())
res = list(itertools.combinations(itertools.chain(letters), K))
count = 0
for i in range(len(res)):
    if 'a' in res[i]:
        count += 1
print(count/(N+K))
# for i in res:
#     print(i)

