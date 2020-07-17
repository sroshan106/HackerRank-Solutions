#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    visited = [100]*101
    queue=[]
    queue.append([1,0])    
    visited[1]=0
    curr=1
    while curr!=100 and queue:
        curr,counter = queue.pop(0)
        for i in range(1,7):
            if (i+curr)<=100 and visited[i+curr]==100:
                if i+curr in ladders:
                    queue.append([ladders[i+curr],counter+1])
                    visited[ladders[i+curr]]=min(visited[ladders[i+curr]],counter+1)
                    visited[i+curr]=min(visited[i+curr],counter+1)
                elif i+curr in snakes:
                    queue.append([snakes[i+curr],counter+1])
                    visited[snakes[i+curr]]=min(visited[snakes[i+curr]],counter+1)
                    visited[i+curr]=min(visited[i+curr],counter+1)
                else:
                    queue.append([i+curr,counter+1])
                    visited[i+curr]=min(visited[i+curr],counter+1)
        
    return visited[100]
            
    


t = int(input())

for t_itr in range(t):
    n = int(input())

    ladders = {}

    for _ in range(n):
        a,b= list(map(int, input().rstrip().split()))
        ladders[a]=b

    m = int(input())

    snakes = {}

    for _ in range(m):
        a,b= list(map(int, input().rstrip().split()))
        snakes[a]=b

    result = quickestWayUp(ladders, snakes)
    if result==100:
        print(-1)
    else:
        print(result)
