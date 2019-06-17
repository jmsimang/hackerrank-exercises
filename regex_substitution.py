#!/usr/bin/python

"""
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for 
each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in
different ways.

TASK
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
    && -> and
    || -> or
Both && and || should have a space ' ' on both sides.

INPUT FORMAT
The first line contains the integer, N.
The bext N lines each contain a line of the text.

CONSTRAINTS
0 < N < 100
Neither && nor || occur in the start or end of each line.

OUTPUT
Output the modified text.
"""

import re

lines = int(input())

def replace(text):
    if text.group() == '&&': return 'and'
    if text.group() == '||': return 'or'

# replace = lambda text: 'and' if text.group() == '&&' else 'or'

for i in range(lines):
    print(re.sub('(?<= )(&&|\|\|)(?= )', replace, input()))

