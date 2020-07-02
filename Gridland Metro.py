#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    track.sort()
    visited=[0]*n
    arr = [0]*m
    prev = track[0][0]
    counter = 0
    for i in range(k):
        r,c1,c2 = track[i]
        for p in range(c1-1,c2):
            arr[p]=1

        if prev!=r:
            visited[r-1]=1    
            counter+= arr.count(0)
            arr=[0]*m
            
        prev=r
    print(counter)
    temp = visited.count(0)
    counter+=temp*m
    return counter

        
nmk = input().split()

n = int(nmk[0])

m = int(nmk[1])

k = int(nmk[2])

track = []

for _ in range(k):
    track.append(list(map(int, input().rstrip().split())))

result = gridlandMetro(n, m, k, track)
print(result)