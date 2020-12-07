#!/usr/bin/env python3
"""
    Day 6 of Advent of Code 2020
"""


def part_two():
    """ Counting answers """
    with open('input') as input:
        inp = input.readlines()

    lines = []
    temp = []
    a = set([chr(i) for i in range(97, 123)])
    for i in range(len(inp)):
        if inp[i] == '\n':
            lines.append(temp)
            temp = []
            continue
        temp.append(inp[i])
    '''print(lines)'''
    lines.append(temp)
    counts = []
    '''lines = [['addddabcba\nbcdddddddddddddddddddddddddddddbcdedf', 'abcdef'], ['abcde', 'bcdeeeaa']]'''
    print(len(lines))
    for i in range(len(lines)):
        temp = ''
        for li in lines[i]:
            temp += li
        print(temp)
        print(set(temp))
        print(len(set(temp)))
        b = a.intersection(set(temp))
        counts.append(len(b))
    print(counts)
    return(sum(counts))


if __name__ == '__main__':
    sum = part_two()
    print("\n\nSum: [{}]".format(sum))
