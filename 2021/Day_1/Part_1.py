#!/usr/bin/env python3


with open('input.txt') as input_text:
    input_text = input_text.readlines()

increased_count = 0
for i in range(1, len(input_text)):
	if int(input_text[i]) > int(input_text[i - 1]):
		increased_count += 1

print(increased_count)