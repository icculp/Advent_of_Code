#!/usr/bin/env python3
"""
    Day 1 of Advent of Code 2020
"""
import requests

def part_two():
    ''' Part two, refactoring to return out of nested loops '''
    with open('./nums') as nums:
        n = nums.read().split('\n')
        n.pop()
    for nu in n:
        for nuu in n:
            for nuuu in n:
                if ((int(nu) + int(nuu) + int(nuuu) == 2020)):
                    print(int(nu) * int(nuu) * int(nuuu))
                    return

if __name__ == '__main__':
    part_two()
