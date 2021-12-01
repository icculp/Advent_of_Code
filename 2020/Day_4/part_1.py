#!/usr/bin/env python3
"""
    Day 3 of Advent of Code 2020
"""


def part_one():
    """ Validate passport data """
    with open('input') as input:
        inp = input.readlines()

    passports = []
    new = []
    for i in range(len(inp)):
        if inp[i][0] == '\n':
            passports.append(new)
            new = []
            continue
        else:
            new.append(inp[i])
    for i in range(len(passports)):
        passports[i] = [passports[i][j].strip('\n').split(' ') for j in range(len(passports[i]))]
        helper = []
        for k in range(len(passports[i])):
            print(passports[i])
            print(passports[i][k])
            helper = [passports[i][k][l].split(':') for l in range(len(passports[i][k]))]
            passports[i][k] = helper
            helper = []
    p = dict()
    print()
    print()
    for i in range(len(passports)):
        for j in range(len(passports[i])):
            for li in passports[i]:
                for lis in li:
                    '''print(lis)'''
                    if p.get(i) is None:
                        p.update({i: {lis[0]: lis[1]}})
                    else:
                        p[i].update({lis[0]: lis[1]})
    print(p)
    count = 0
    for key in p.keys():
        if len(p[key].keys()) == 8:
            count += 1
        elif len(p[key].keys()) == 7 and 'cid' not in p[key].keys():
            count += 1
        else:
            continue

    return count


if __name__ == '__main__':
    count = part_one()
    print("\n\nCount: [{}]".format(count))
