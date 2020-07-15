#!/bin/python3

import math
import os
import random
import re
import sys
def groups(cities,visited,root):
    queue=[]
    queue.append(root)
    while queue:
        x=queue.pop(0)
        if x in cities:
            nodes = cities[x]
            for i in nodes:
                if visited[i]==0:
                    queue.append(i)
                    visited[i]=1 
    return 
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return n*c_lib
    visited=[0]*n
    counter=0
    for i in range(n):
        if visited[i]==0:
            groups(cities,visited,i)
            counter+=1
    edges=n-counter
    return  counter*c_lib+edges*c_road
q = int(input())

for q_itr in range(q):
    nmC_libC_road = input().split()

    n = int(nmC_libC_road[0])

    m = int(nmC_libC_road[1])

    c_lib = int(nmC_libC_road[2])

    c_road = int(nmC_libC_road[3])

    cities = {}

    for _ in range(m):
        v1,v2=list(map(int, input().rstrip().split()))
        v1-=1
        v2-=1
        if v1 not in cities:
            cities[v1]=[v2]
        else:
            cities[v1].append(v2)
        if v2 not in cities:
            cities[v2]=[v1]
        else:

            cities[v2].append(v1)


    result = roadsAndLibraries(n, c_lib, c_road, cities)
    
    print(result)

