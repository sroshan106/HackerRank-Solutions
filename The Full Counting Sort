#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    l=[]
    for i in range(100):
        l.append([])
    n= len(arr)
    for i in range(n):
        a,b = arr[i][0],arr[i][1]
        a=int(a)
        if i<n//2:
            b='-'
        l[a].append(b)
        
        
    result=''
    for i in l:
        for k in i:
            result+=k+' '
    print(result)
if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
