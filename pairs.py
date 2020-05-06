#!/bin/python3

# Complete the pairs function below.
def pairs(k, arr):
    arr= set(arr)
    count=0
    for i in arr:
        if(i+k in arr):
            count+=1
    return count
        

nk = input().split()

n = int(nk[0])

k = int(nk[1])

arr = list(map(int, input().rstrip().split()))

result = pairs(k, arr)
print(result)
