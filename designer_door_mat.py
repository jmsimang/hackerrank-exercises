"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Input Format
A single line containing the space separated values of N and M.

Constraints
5 < N < 101
15 < M < 303

Output Format
Output the design pattern.

"""
N, M = map(int, input().split())

top = []
bottom = []
for i in range(N//2):
    top.append(('.|.' * (2 * i + 1)).center(M, '-'))
    bottom.append(('.|.' * (2 * i + 1)).center(M, '-'))
bottom = bottom[::-1]

for i in range(len(top)):
    print(top[i])
print('WELCOME'.center(M, '-'))
for i in range(len(bottom)):
    print(bottom[i])
