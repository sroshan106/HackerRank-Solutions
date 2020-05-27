#!/bin/python3

import math
import os
import random
import re
import sys
def swap(arr,b):
    c=[]
    count=0
    for i in range(len(arr)):
        if b[i]!=arr[i]:
            count+=1
            c.append(i)
    if count==2:
        print("yes")
        print("swap",c[0]+1,c[1]+1)
        return True
    return False

    
def reversal(arr,b):
    start=-1
    end=0
    for i in range(len(arr)):
        if b[i]!=arr[i] and start==-1:
            start=i
        if b[i]!=arr[i]:
            end=i
    e=arr[:start]
    f=arr[start:end+1]
    f.reverse()
    g=arr[end+1:]
    arr = e+f+g
    if arr==b:
        print("yes")
        print("reverse",start+1,end+1)
        return True
    else:
        return False
def almostSorted(arr):
    b=arr[:]
    b.sort()
    if b==arr:
        print("yes")
    else:
        if swap(arr,b)==False:
            if reversal(arr,b)==False:
                print("no")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
