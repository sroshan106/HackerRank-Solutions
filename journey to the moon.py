#!/bin/python3

import math
import os
import random
import re
import sys
def pairs(ast,root,visited):
    queue=[]
    temp=set()
    queue.append(root)
    temp.add(root)
    while queue:
        x = queue.pop(0)
        if x in ast:
            l = ast[x]
            for i in l:
                if visited[i]==0:
                    queue.append(i)
                    visited[i]=1
                    temp.add(i)
    return len(temp)

def journeyToMoon(n, ast):
    visited=[0]*n
    temp=[]
    for i in range(n):
        if visited[i]==0:
            p = pairs(ast,i,visited)
            temp.append(p)
    length = len(temp)
    
    counter=0
    for i in range(length):
        for j in range(i+1,length):
            counter+=temp[i]*temp[j]
    return counter
np = input().split()

n = int(np[0])

p = int(np[1])

ast = {}

for _ in range(p):
    a,b =list(map(int, input().rstrip().split()))
    if a not in ast:
        ast[a]=[b]
    else:
        ast[a].append(b)
    if b not in ast:
        ast[b]=[a]
    else:
        ast[b].append(a)

result = journeyToMoon(n, ast)

print(result)
