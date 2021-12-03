#!/usr/bin/env python3


with open('input.txt') as input_text:
    input_text = input_text.readlines()

depth = horizontal = 0
for i in range(len(input_text)):
    direction, value = input_text[i].split()
    value = int(value)
    if direction == 'up':
        depth -= value
    elif direction == 'down':
        depth += value
    elif direction == 'forward':
        horizontal += value

print(horizontal * depth)