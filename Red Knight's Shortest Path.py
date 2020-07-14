#!/bin/python3

import math
import os
import random
import re
import sys
def isSafe(x,y):
    global n
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False

def printShortestPath(n, i_start, j_start, i_end, j_end):
    visited=[]
    for i in range(n):
        visited.append([0]*n)
    queue=[]
    moves=[[-2,-1],[2,1],[0,2],[2,1],[2,-1],[0,-2]]
    visited[i_start][j_start]=1
    queue.append([i_start,jstart])
    while queue:
        x,y = queue.pop()
        for i in moves:
            m,n = i
            if isSafe(x+m,y+n)



n = int(input())

i_startJ_start = input().split()

i_start = int(i_startJ_start[0])

j_start = int(i_startJ_start[1])

i_end = int(i_startJ_start[2])

j_end = int(i_startJ_start[3])

printShortestPath(n, i_start, j_start, i_end, j_end)
