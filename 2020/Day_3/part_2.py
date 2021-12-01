#!/usr/bin/env python3
"""
    Day 3 of Advent of Code 2020
"""


def part_one(right, down):
    """ Count trees on differing slopes (m)
        m = right/down
        so right is the right step, and down is the down step
    """
    with open('input') as input:
        inp = input.readlines()

    lines = []
    tree = right
    tree_count = 0
    start = down
    for i in range(start, len(inp), down):
        if inp[i][tree % 31] == '#':
            tree_count += 1
        tree += right
    return tree_count


if __name__ == '__main__':
    one_one = part_one(1, 1)
    print(one_one)
    three_one = part_one(3, 1)
    print(three_one)
    five_one = part_one(5, 1)
    print(five_one)
    seven_one = part_one(7, 1)
    print(seven_one)
    one_two = part_one(1, 2)
    print(one_two)
    multiple = one_one * three_one * five_one * seven_one * one_two
    print(multiple)
