#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    s = list(s)
    mid = n//2-1
    counter=0
    for i in range(mid+1):
        if s[i] != s[n-1-i]:
            counter+=1    
    if counter>k:
        return -1

    for i in range(mid+1):
        if s[i] != s[n-1-i]:
            if counter<k and s[i]!='9':
                s[i]=s[n-i-1]='9'
                k-=2
                counter-=1
            else:
                maxx = max(s[i],s[n-1-i])
                s[i]=s[n-1-i]=maxx
                k-=1
                counter-=1
    i=0
    while(k>=2 and i<n):
        if s[i]!='9':
            s[i]='9'
            s[n-i-1]='9'
            k-=2
        i+=1

    if n%2==1 and k==1:
        s[mid+1]='9'

            
    return ''.join(s)



    return ''.join(s)
nk = input().split()

n = int(nk[0])

k = int(nk[1])

s = input()

result = highestValuePalindrome(s, n, k)

print(result)
