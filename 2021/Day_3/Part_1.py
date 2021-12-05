#!/usr/bin/env python3
import numpy as np
from scipy import stats

with open('input.txt') as input_text:
    input_text = input_text.readlines()

arr = np.array([[eval(x) for x in line.strip('\n')] for line in input_text])
epsilon = stats.mode(arr).mode
gamma = 1 - epsilon
epsilon = epsilon.dot(2 ** np.arange(epsilon.size)[::-1])[0]
gamma = gamma.dot(2 ** np.arange(gamma.size)[::-1])[0]
print(epsilon * gamma)