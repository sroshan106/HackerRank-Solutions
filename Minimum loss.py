#!/bin/python3

import math
import os
import random
import re
import sys


def minimumLoss(price):
    n = len(price)
    arr =[]
    for i in range(n):
        arr.append([price[i],i])
    arr.sort()
    minn = arr[1][0]-arr[0][0]
    for i in range(n-1):
        value,index = arr[i+1]
        pvalue,pindex =arr[i]
        temp = value-pvalue
        if index<pindex:
            minn = min(minn,temp)

    return  minn
    
n = int(input())

price = list(map(int, input().rstrip().split()))

result = minimumLoss(price)
print(result)
