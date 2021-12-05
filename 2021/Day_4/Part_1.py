#!/usr/bin/env python3
import numpy as np

with open('input.txt') as input_text:
    input_text = input_text.readlines()

numbers = [eval(x) for x in input_text[0].strip('\n').split(',')]
arr = np.array([])
new = None
for line in input_text[1:]:
    line = line.strip()
    if len(line) < 1:
        if new is not None:
            arr = np.append(arr, new).astype(np.int)
        new = np.array([])
    else:
        new = np.append(new, [line.split()]).reshape((-1, 5))

arr = arr.reshape((-1, 5, 5))

def do():
    for number in numbers:
        for i in range(len(arr)):
            arr[i][np.where(arr[i] == number)] = 0
            if np.all((arr[i] == 0), axis=1).any():
                return number * arr[i].sum().sum()  
            if np.all((arr[i] == 0), axis=0).any():
                return number * arr2[i].sum().sum()  
print(do())
