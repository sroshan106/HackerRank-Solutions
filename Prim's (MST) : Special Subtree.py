
import sys
def minKey(key, mstSet,n): 
    minn = sys.maxsize
    min_index=-1
    for v in range(n): 
        if key[v] < minn and mstSet[v] == False: 
            minn = key[v] 
            min_index = v 
    return min_index 


def prims(n, matrix,start):
    key= [sys.maxsize]*n
    #print(key)
    parent = [None]*n
    key[start]=0
    mstSet = [False]*n
    parent[start]=-1

    for i in range(n):
        u = minKey(key,mstSet,n)
        mstSet[u]=True  
        for v in range(n):
            if matrix[u][v]>-1 and mstSet[v]==False and key[v]>matrix[u][v]:
                key[v]=matrix[u][v]
                parent[v]=u

    return sum(key)


nm = input().split()

n = int(nm[0])

m = int(nm[1])

#edges = []

matrix=[]
for i in range(n):
    matrix.append([-1]*n)

for _ in range(m):
    a,b,weight= (list(map(int, input().rstrip().split())))
    a-=1
    b-=1
    if matrix[a][b]!=-1:
        matrix[a][b]=min(matrix[a][b],weight)
        matrix[b][a]=min(matrix[b][a],weight)
    else:
        matrix[a][b]=weight
        matrix[b][a]=weight

start = int(input())
start-=1
result = prims(n, matrix,start)

print(result)
