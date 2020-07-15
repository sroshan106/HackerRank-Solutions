#!/bin/python3

from collections import deque
def pairs(ast,root,visited):
    queue = deque([])
    queue.append(root)
    visited[root]=1
    temp=1
    while queue:
        x = queue.popleft()
        if x in ast:
            l = ast[x]
            for i in l:
                if visited[i]==0:
                    queue.append(i)
                    visited[i]=1
                    temp+=1
    return temp

def journeyToMoon(n, ast):
    visited=[0]*n
    temp=[]
    for i in range(n):
        if visited[i]==0:
            p = pairs(ast,i,visited)
            temp.append(p)
    length = len(temp)
    counter=(n*(n-1))//2
    for i in temp:
        if i>1:
            counter-=((i*(i-1))//2)
    return counter
np = input().split()

n = int(np[0])

p = int(np[1])

ast = {}

for _ in range(p):
    a,b =list(map(int, input().rstrip().split()))
    if a not in ast:
        ast[a]=[b]
    else:
        ast[a].append(b)
    if b not in ast:
        ast[b]=[a]
    else:
        ast[b].append(a)

result = journeyToMoon(n, ast)

print(result)
