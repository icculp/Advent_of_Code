#!/usr/bin/env python3
import numpy as np
from scipy import stats

with open('input.txt') as input_text:
    input_text = input_text.readlines()

# Since ties resort to lower value, we replaced 0's with 2's
arr = np.array([[eval(x) if x == '1' else 2 for x in line.strip('\n')] for line in input_text])

common = stats.mode(arr).mode[0]
length = len(common)
common = common[0]
least = 2 if common == 1 else 1
Oxygen_generator_rating = arr[np.where(arr[:,0] == common)]
CO2_scrubber_rating = arr[np.where(arr[:,0] == least)]
for i in range(1, length - 1):
    if len(Oxygen_generator_rating) > 1:
        common = stats.mode(Oxygen_generator_rating).mode[0][i]
        Oxygen_generator_rating = Oxygen_generator_rating[np.where(Oxygen_generator_rating[:,i] == common)]
    if len(CO2_scrubber_rating) > 1:
        least = stats.mode(CO2_scrubber_rating).mode[0][i]
        least = 2 if least == 1 else 1
        CO2_scrubber_rating = CO2_scrubber_rating[np.where(CO2_scrubber_rating[:,i] == least)]
    
Oxygen_generator_rating[np.where(Oxygen_generator_rating == 2)] = 0# np.array([x if x is 1 else 0 for x in Oxygen_generator_rating])
CO2_scrubber_rating[np.where(CO2_scrubber_rating == 2)] = 0# np.array([x if x is 1 else 0 for x in CO2_scrubber_rating])
Oxygen_generator_rating = Oxygen_generator_rating.dot(2 ** np.arange(Oxygen_generator_rating.size)[::-1])[0]
CO2_scrubber_rating = CO2_scrubber_rating.dot(2 ** np.arange(CO2_scrubber_rating.size)[::-1])[0]
life_support_rating = Oxygen_generator_rating * CO2_scrubber_rating
print(life_support_rating)
