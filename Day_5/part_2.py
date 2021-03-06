#!/usr/bin/env python3
"""
    Day 5 of Advent of Code 2020
"""


def part_two():
    """ Decode boarding pass identifiers using binary space partitioning """
    with open('input') as input:
        inp = input.readlines()

    passes = []

    ''' Initial test to get stead id of a single pass
    f = 'FBFBBFFRLR'
    temp = ''
    for i in range(7):
        if f[i] == 'B':
            temp += '1'
        elif f[i] == 'F':
            temp += '0'
    row = int(temp, 2)
    print(row)
    temp = ''
    for j in range(7, 10):
        if f[j] == 'R':
            temp +='1'
        elif f[j] == 'L':
            temp += '0'
    col = int(temp, 2)
    print(col)
    seat_id = row * 8 + col
    print(seat_id)
    '''
    for i in range(len(inp)):
        temp = ''
        for j in range(7):
            if inp[i][j] == 'B':
                temp += '1'
            elif inp[i][j] == 'F':
                temp += '0'
        row = int(temp, 2)
        temp = ''
        for j in range(7, 10):
            if inp[i][j] == 'R':
                temp +='1'
            elif inp[i][j] == 'L':
                temp += '0'
        col = int(temp, 2)
        seat_id = row * 8 + col
        '''print(seat_id)'''
        passes.append(seat_id)

    passes.sort()
    for i in range(len(passes) - 1):
        if (passes[i + 1] - passes[i]) > 1:
            my_seat = passes[i] + 1
    print(my_seat)
    return my_seat



if __name__ == '__main__':
    my_seat = part_two()
    print("\n\nMy seat: [{}]".format(my_seat))
