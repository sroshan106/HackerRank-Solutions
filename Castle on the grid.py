#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY,n):
    visited=[]
    for i in range(n):
        visited.append([100000]*n)
    queue=[]
    counter=0
    queue.append([startX,startY,counter])
    visited[startX][startY]=0
    while queue:
        curX,curY,counter = queue.pop(0)
        if curX==goalX and curY==goalY:
            return visited[curX][curY]
        temp = curX+1
        while temp<n and grid[temp][curY]!='X':
            if visited[temp][curY]==100000:
                queue.append([temp,curY,counter+1])
            
            visited[temp][curY]=min(visited[temp][curY],counter+1)
            temp+=1
            

        temp = curX-1
        while temp>=0 and grid[temp][curY]!='X':
            if visited[temp][curY]==100000:
                queue.append([temp,curY,counter+1])
            
            visited[temp][curY]=min(visited[temp][curY],counter+1)
            temp-=1
            

        
        temp = curY+1
        while temp<n and grid[curX][temp]!='X':
            if visited[curX][temp]==100000:
            
                queue.append([curX,temp,counter+1])
            
            visited[curX][temp]=min(visited[curX][temp],counter+1)
            temp+=1
            

        temp = curY-1
        while temp>=0 and grid[curX][temp]!='X':
            if visited[curX][temp]==100000:
                queue.append([curX,temp,counter+1])
            visited[curX][temp]=min(visited[curX][temp],counter+1)
            temp-=1
            


n = int(input())

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

startXStartY = input().split()

startX = int(startXStartY[0])

startY = int(startXStartY[1])

goalX = int(startXStartY[2])

goalY = int(startXStartY[3])

result = minimumMoves(grid, startX, startY, goalX, goalY,n)
print(result)
