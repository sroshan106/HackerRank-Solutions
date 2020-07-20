import sys


def findMin(distance,visited,n):
    minVal = sys.maxsize
    minIndex = -1
    for i in range(n):
        if visited[i]==False and distance[i]<minVal:
            minVal = distance[i]
            minIndex = i
    return minIndex


def dijsktra(mat,n,source,destination):
    distance =[sys.maxsize]*n
    visited=[False]*n
    distance[source]=0
    #print(distance)
    for _ in range(n-1):
        minVertex = findMin(distance,visited,n)
        visited[minVertex]=True
        for j in range(n):
            if mat[minVertex][j]!=-1 and not visited[j]:
                dist = distance[minVertex]+mat[minVertex][j]
                if dist<distance[j]:
                    distance[j]=dist

    return distance

n = int(input())
m = int(input())
mat = []
for i in range(n):
    mat.append([-1]*n)

for _ in range(m):
    a,b,weight = list(map(int,input().split(" ")))
    if mat[a][b]==-1:
        mat[a][b]=weight
    else:
        if mat[a][b]>weight:
            mat[a][b]=weight

    mat[b][a]=mat[a][b]
    
source,destination = list(map(int,input().split(" ")))

print(dijsktra(mat,n,source , destination))
