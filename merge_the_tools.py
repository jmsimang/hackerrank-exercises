"""
Consider the following:

A string, `s`, of length `n` where `s = c0c1...cn-1`.
An integer, `k`, where `k` is a factor of `n`.
We can split `s` into `n / k` subsegments where each subsegment, `Ti`, consists of a contiguous block of `k` 
characters in `s`. Then, use each `Ti` to create string `Ui` such that:

The characters in `Ui` are a subsequence of the characters in `Ti`.
Any repeat occurrence of a character is removed from the string such that each character in `Ui` occurs exactly once. 
In other words, if the character at some index `j` in `Ti` occurs at a previous index < `j` in `Ti`, 
then do not include the character in string `Ui`.
Given `s` and `k`, print `n / k` lines where each line `i` denotes string .

Input Format
The first line contains a single string denoting `s`. 
The second line contains an integer, `k`, denoting the length of each subsegment.

Constraints
1 <= n <= 10^4, where `n` is the length of `s`.
It is guaranteed that `n` is a multiple of `k`.

Output Format
Print `n/k` lines where each line `i` contains string `Ui`.
"""

def merge_the_tools(string, k):
    # your code goes here
    str_list = [string[i:i+k] for i in range(0, len(string), k)]
    final = []
    for s in str_list:
        for i in range(len(s)):
            value = s[i]
            for j in range(len(s)):
                if (s[j] != s[i]) and (s[j] not in value):
                    value += s[j]
            final.append(value)
    for i in range(0, len(final), k):
        print(final[i])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
