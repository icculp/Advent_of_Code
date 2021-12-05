#!/usr/bin/env python3
import numpy as np

with open('input.txt') as input_text:
    input_text = input_text.readlines()

numbers = np.array([[eval(x) for x in line.strip('\n').split(' -> ')] for line in input_text]).reshape((-1, 4))
crossed = np.zeros((numbers.max(), numbers.max()))
for line in numbers:
    x1, y1, x2, y2 = line - 1
    print('here')
    # print(type(x1.val))
    print(x1, x2, y1, y2)
    if x1 == x2:
        crossed[x1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += 1
    if y1 == y2:
        crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, y1] += 1

print(np.array(np.where(crossed > 1)).shape)