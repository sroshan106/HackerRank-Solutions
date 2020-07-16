import sys
sys.setrecursionlimit(6000)
def compare(element):
    smallest = element[2]
    summ = element[0]+element[1]+element[2]
    return (smallest,summ)

def root(element,parent):
    if parent[element]==element:
        return element
    return root(parent[element],parent)

def krus(n,e,edges):
    edges = sorted(edges,key=compare)
    #print(edges)
    summ=0
    parent =  [0]*n
    for i in range(n):
        parent[i]=i
    counter=0
    
    for i in range(e):
        source,destination,weight = edges[i]
        sourceParent = root(source,parent)
        destinationParent = root(destination,parent)
        if sourceParent!=destinationParent:
            summ+=weight
            parent[sourceParent]=destinationParent
            
    return summ



n , e = map(int,input().split(" "))
edges=[]
for _ in range(e):
    a,b,c = list(map(int,input().split(" ")))
    a-=1
    b-=1
    edges.append([a,b,c])
result = krus(n,e,edges)
print(result)
