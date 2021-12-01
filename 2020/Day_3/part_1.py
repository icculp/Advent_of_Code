#!/usr/bin/env python3
"""
    Day 3 of Advent of Code 2020
"""


def part_one():
    """ Count trees on slope -3 """
    with open('input') as input:
        inp = input.readlines()

    lines = []
    tree = 3
    tree_count = 0
    for i in range(1, len(inp)):
        if inp[i][tree % 31] == '#':
            tree_count += 1
        tree += 3
    print(tree_count)


if __name__ == '__main__':
    part_one()
