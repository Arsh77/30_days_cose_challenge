#!/bin/python3

import sys


arr = []
for arr_i in range(6):   
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
a=len(arr)
b=len(arr[0])
s=[]
for i in range(a):
    for j in range(b):
        if i+2<a and j+2<b:
            sum1 = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            s.append(sum1)
        else:
            pass
print(max(s))
        
