#!/usr/bin/env python3


with open('input.txt') as input_text:
    input_text = input_text.readlines()

depth = horizontal = aim = 0
for i in range(len(input_text)):
    direction, value = input_text[i].split()
    value = int(value)
    if direction == 'up':
        #depth -= value
        aim -= value
    elif direction == 'down':
        #depth += value
        aim += value
    elif direction == 'forward':
        horizontal += value
        depth += (aim * value)

print(horizontal * depth)