#!/usr/bin/python

"""
TEXT ALIGNMENT - Strings in Python
.ljust(width) - returns a left aligned string of length width.
.center(width) - returns a centered string of length width.
.rjust(width) - returns a right aligned string of length width.

TASK
You are given partial code that is used for generating the HackerRank Logo of variable
thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

INPUT FORMAT
A single line containing the thickness value of the logo.

CONSTRAINTS
The thickness must be an odd number
0 < thickness < 50

OUTPUT FORMAT
Output the desired logo.
"""

thickness = int(input())
c = 'H'

#Top cone
for i in range(thickness):
    print((c*i).rjust(thickness-i) + c + (c*i).ljust(thickness-i))

#Top pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

