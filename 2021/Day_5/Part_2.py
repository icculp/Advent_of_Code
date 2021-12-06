#!/usr/bin/env python3
import numpy as np

with open('input.txt') as input_text:
    input_text = input_text.readlines()

numbers = np.array([[eval(x) for x in line.strip('\n').split(' -> ')] for line in input_text]).reshape((-1, 4))
crossed = np.zeros((numbers.max() + 1, numbers.max() + 1))
for line in numbers:
    x1, y1, x2, y2 = line
    if x1 == x2:
        crossed[x1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += 1
    elif y1 == y2:
        crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, y1] += 1
    else:
        diag = np.eye(abs(x1 - x2) + 1)
        if x2 > x1 and y2 > y1:
            crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += diag
        elif x1 > x2 or y1 > y2:
            if x1 > x2:
                if y1 > y2:
                    crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += diag
                else:
                    crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += np.flip(diag, axis=1)
            elif y1 > y2:
                crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += np.flip(diag, axis=1)
print(crossed.T)
print(np.array(np.where(crossed > 1)).shape[-1])
# 15140
# 14501
# 15342

# 17193 actual...
