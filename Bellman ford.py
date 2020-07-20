import sys
def bellman(n,m,edges,source):
    distance=[sys.maxsize]*n
    distance[source]=0
    for _ in range(n-1):
        for i in edges:
            start,end,weight = i
            if distance[start]!=sys.maxsize:
                temp = distance[start]+weight
                if distance[end]>temp:
                    distance[end]=temp

    return distance
n = int(input())
m = int(input())
edges=[]
for _ in range(m):
    edges.append(list(map(int,input().split(" "))))
source=0
print(bellman(n,m,edges,source))
