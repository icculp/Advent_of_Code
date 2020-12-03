#!/usr/bin/env python3
"""
    Day 2 of Advent of Code 2020
"""


with open('input') as input:
    '''print(dir(input))'''
    inp = input.readlines()
    '''print(type(inp))
    print(inp)'''

lines = []
valid_count = 0
for i in range(len(inp)):
    lines.append(inp[i].split(' '))
    lines[i][0] = lines[i][0].split('-')
    '''lines[i].append(lines[i][2].count(lines[i][1][0]))'''
    c = 0
    if lines[i][1][0] == lines[i][2][eval(lines[i][0][0]) - 1]:
        c += 1
    if lines[i][1][0] == lines[i][2][eval(lines[i][0][1]) - 1]:
        c += 1
    if c == 1:
        valid_count += 1
    
    '''if lines[i][3] >= eval(lines[i][0][0]) and lines[i][3] <= eval(lines[i][0][1]):
    
        valid_count += 1'''

print(valid_count)


'''
for i in range(len(lines)):
    lines[i]

print(lines)
'''
