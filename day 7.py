#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a= list(reversed(arr))
for x in a:
    print(x, end=' ')
