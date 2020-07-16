def third(elem):
    return elem[2]

def kruskals(g_nodes, g):
    g = sorted(g,key = third)
    visited=[0]*g_nodes
    summ=0
    counter=0
    for i in g:
        to,From,weight = i
        if to!=From:
            if visited[to]!=1 or visited[From]!=1:
                counter+=1
                summ+=weight
                if visited[to]==0:
                    visited[to]=1
                    
                if visited[From]==0:
                    visited[From]=1
                    
        if counter==g_nodes-1:
            break
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
