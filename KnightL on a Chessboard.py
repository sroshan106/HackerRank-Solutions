#!/bin/python3

import math
import os
import random
import re
import sys
def steps(i,j,n):
    x =y =counter=0
    visited =[]
    for _ in range(n):
        visited.append([0]*n)

    pos =[[i,j],[i,-j],[-i,j],[-i,-j],[j,i],[j,-i],[-j,i],[-j,-i]]
    queue=[]
    queue.append([x,y,counter])
    visited[0][0]=1

    while queue and (x!=n-1 or y!=n-1):
        x,y,counter = queue.pop(0)
        for p in pos:
            i,j = p
            if x+i>=0 and x+i<n and y+j>=0 and y+j<n:
                if visited[x+i][y+j]==0:
                    visited[x+i][y+j]=1
                    queue.append([x+i,y+j,counter+1])
    
    
    if queue==[] and (x!=n-1 or y!=n-1):
        return -1
    return counter
                    
    

def knightlOnAChessboard(n):
    
    for i in range(1,n):
        for j in range(1,n):
            result = steps(i,j,n)
            print(result,end =" ")
        print()
    
    '''
    result = steps(3,4,n)
    print(result,end =" ")

    '''
n = int(input())

result = knightlOnAChessboard(n)


