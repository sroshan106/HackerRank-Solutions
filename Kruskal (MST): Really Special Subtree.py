import sys
sys.setrecursionlimit(5000)

def third(elem):
    small = elem[2]
    summ = elem[0]+elem[1]+elem[2]
    return (small,summ)


def findParent(element ,parent):
    if parent[element]==element:
        return element
    return findParent(parent[element],parent)


def kruskals(n, edge):
    edge = sorted(edge,key = third)
    #print(edge)
    
    output =[0]*(n-1)

    parent=[0]*n
    for i in range(n):
        parent[i]=i
    counter=0
    i=0
    while counter!=n-1:
        source,destination,weights = edge[i]
        sourceParent = findParent(source,parent)
        destinationParent =  findParent(destination,parent)
        if  sourceParent!=destinationParent:
            output[counter]=[source,destination,weights]
            counter+=1
            parent[source]=destinationParent
        i+=1
    summ=0
    for i in output:
       summ+=i[2]
    return summ
    

g_nodes, g_edges = map(int, input().rstrip().split())
g=[]
for i in range(g_edges):
    g.append([0]*3)

for i in range(g_edges):
    g[i][0], g[i][1], g[i][2] = map(int, input().rstrip().split())
    
    g[i][0]-=1
    g[i][1]-=1
    
res = kruskals(g_nodes, g)

print(res)
