#!/usr/bin/env python3
import numpy as np

with open('input.txt') as input_text:
    input_text = input_text.readlines()

numbers = np.array([[eval(x) for x in line.strip('\n').split(' -> ')] for line in input_text]).reshape((-1, 4))
crossed = np.zeros((numbers.max() + 1, numbers.max() + 1))
for line in numbers:
    x1, y1, x2, y2 = line
    #print('here')
    # print(type(x1.val))
    #print(x1, x2, y1, y2)
    if x1 == x2:
        crossed[x1, np.minimum(y1, y2): np.maximum(y1, y2) + 1] += 1
    elif y1 == y2:
        crossed[np.minimum(x1, x2): np.maximum(x1, x2) + 1, y1] += 1
    else:
        ones = np.ones(crossed.shape)
        diag = np.diag(ones)
        np.diag(np.ones(4),1)
        if abs(x1 - x2) != abs(y1 - y2):
            print('wtf')
        if x2 > x1 and y2 > y1:
            #print(11111111111, x1, y1, x2, y2)
            diag = np.eye(x2 - x1 + 1)
            #print(diag)
            crossed[x1:x2 + 1, x1:x2 + 1] += diag
        elif x1 > x2 or y1 > y2:
            #print(2, x1, y1, x2, y2)
            if x1 > x2:
                diag = np.eye(x1 - x2 + 1)
                if y1 > y2:
                    crossed[x2 - 1:x1, y2:y1 + 1] += np.flip(diag, axis=1)
                else:
                    #print(x1, x2, y1, y2)
                    #print(np.flip(diag, axis=1).shape)
                    #print(crossed[x2:x1 + 1, y1:y2 + 1].shape)
                    crossed[x2:x1 + 1, y1:y2 + 1] += np.flip(diag, axis=0)
            elif y1 > y2:
                diag = np.eye(y1 - y2 + 1)
                #print(np.flip(diag, axis=1))
                crossed[x1:x2 + 1, y2:y1+1] += np.flip(diag, axis=0 )
            #print(diag.shape)
            #print(crossed[x2:x1 + 1].shape)
        else:
            print('NOOOOOOOOOOO')
print(crossed)
print(np.array(np.where(crossed > 1)).shape)
# 15140
# 14501
# 15342

# 17193 actual...


# borrowed from https://www.reddit.com/r/adventofcode/comments/r9824c/2021_day_5_solutions/hnd3a5v/?utm_source=reddit&utm_medium=web2x&context=3
grid = np.zeros((2, 1000, 1000))
#ls = np.fromregex(open(0), '\d+', [('',int)]*4)

for (x, y, X, Y) in numbers:
    dx, dy = np.sign([X-x, Y-y])                 
    while (x,y) != (X+dx, Y+dy):
        grid[dx * dy, x, y] += 1
        x+=dx; y+=dy

print((grid[0]>1).sum(), (grid.sum(0)>1).sum())