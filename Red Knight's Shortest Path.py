#!/bin/python3

import math
import os
import random
import re
import sys
def isSafe(x,y,visited):
    global n
    if x>=0 and x<n and y>=0 and y<n and visited[x][y]==[]:
        return True
    return False

def printShortestPath(n, i_start, j_start, i_end, j_end):
    d={0:'UL',1:'UR',2:'R',3:'LR',4:'LL',5:'L'}
    visited=[]
    for i in range(n):
        visited.append([[]]*n)
    queue=[]
    moves=[[-2,-1],[-2,1],[0,2],[2,1],[2,-1],[0,-2]]
    visited[i_start][j_start]=[0]
    queue.append([0,i_start,j_start])
    while queue:
        counter,x,y = queue.pop(0)
        if x==i_end and y==j_end:
            return visited[x][y]
        for i in range(6):
            m,n = moves[i]
            if isSafe(x+m,y+n,visited):
                queue.append([counter+1,x+m,y+n])
                if visited[x+m][y+n]!=[]:
                    count= visited[x+m][y+n][0]
                    if count>counter+1:
                        visited[x+m][y+n]=visited[x][y].copy()
                        visited[x+m][y+n][0]=counter+1
                        visited[x+m][y+n].append(d[i])
                    else:
                        visited[x+m][y+n].append(d[i])
                        visited[x+m][y+n][0]+=1

                else:
                    visited[x+m][y+n]=visited[x][y].copy()
                    visited[x+m][y+n][0]+=1
                    visited[x+m][y+n].append(d[i])
        #print(queue)
        #print('#',visited)
    return -1


n = int(input())

i_startJ_start = input().split()

i_start = int(i_startJ_start[0])

j_start = int(i_startJ_start[1])

i_end = int(i_startJ_start[2])

j_end = int(i_startJ_start[3])

temp = printShortestPath(n, i_start, j_start, i_end, j_end)
if temp==-1:
    print("Impossible")
else:
    print(temp[0])
    for i in range(1,temp[0]+1):
        print(temp[i],end=" ")
