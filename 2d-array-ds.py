#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

k = 0
i = 0
j = 0
sum = 0
while (i < 3 and j < 6):
    if (i == 2):
        if(j == 0 or j == 2):
            sum = sum + arr[i][j]
            print(sum)
    if (j == (0 or 1 or 2)):
        sum = sum + arr[i][j]
print(sum)        
