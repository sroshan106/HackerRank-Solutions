
import sys
sys.setrecursionlimit(10**6)
def findRoot(edges):
    n = len(edges)
    for i in range(n):
        if len(edges[i])>1:
            return i

def dfs(node):
    global visited,valueNode,data,edges
    if visited[node]==1:
        return 0
    if len(edges[node])==1:
        valueNode[node]=data[node]
        visited[node]=1
        return valueNode[node]
    else:
        temp=data[node]
        visited[node]=1
        for i in edges[node]:
            temp+=dfs(i)
        valueNode[node] =temp
        return valueNode[node]


def diff(val,summ):
    return abs(summ-2*val)
    


n = int(input().strip())

data = list(map(int, input().rstrip().split()))
edges =[]
for i in range(n):
    edges.append([])

for _ in range(n - 1):
    a,b = list(map(int, input().rstrip().split()))
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
root =  findRoot(edges)
visited=[0]*n
valueNode=[0]*n
dfsValues = dfs(root)
summ = sum(data)
#print(summ)
#print(valueNode)
temp=[0]*n
for i in range(n):
    temp[i]=diff(valueNode[i],summ)
print(min(temp))
