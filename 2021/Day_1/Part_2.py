#!/usr/bin/env python3

with open('input.txt') as input_text:
    input_text = input_text.readlines()

increased_count = 0
for i in range(4, len(input_text) + 1):
    wndo1 = sum(int(x) for x in input_text[i - 4: i - 1])
    wndo2 = sum(int(y) for y in input_text[i - 3: i])
    if wndo2 > wndo1:
        increased_count += 1

print(increased_count)