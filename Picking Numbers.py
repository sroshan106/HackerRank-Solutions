#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    d ={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    temp= 0
    prev= 0
    prevkey=0
    maxx = max(d.values())
    for i in sorted(d.keys()):
        if(prevkey+1==i):
            if temp< d[i]+prev:
                temp = d[i]+prev
        prev=d[i]
        prevkey = i
    
    if temp<maxx:
        return maxx
    return temp

n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)
print(result)
