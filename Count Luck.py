#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countLuck function below.
def countLuck(matrix,n,m,k):
    visited=[]
    for i in range(n):
        visited.append([0]*m)

    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='M':
                x=i
                y=j
                break
    moves= [[1,0],[0,1],[-1,0],[0,-1]]
    queue=[]
    counter =0
    queue.append([x,y,counter])
    while queue:
        x,y,counter = queue.pop(0)
        temp=[]
             
        if matrix[x][y]=='*':
            return counter
            
        for i in moves:
            hor,ver = i
            hor = x+hor
            ver = y+ver
            
            if hor>=0 and hor<n and ver>=0 and ver<m:
                
                if (matrix[hor][ver]=='.' or matrix[hor][ver]=='*') and visited[hor][ver]==0:
                    visited[hor][ver]=1
                    temp.append([hor,ver,counter])
        q = len(temp)
        if q>1:
            for i in range(q):
                temp[i][2]+=1
        
        queue+=temp


t = int(input())

for t_itr in range(t):
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    k = int(input())

    result = countLuck(matrix,n,m,k)
    
    if result ==k:
        print("Impressed")
    else:
        print("Oops!")
