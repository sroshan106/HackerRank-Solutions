def dfs(node,visited,counter):
    counter=0
    global d,result
    visited[node]=1
    print(node)
    if node in d:
        arr = d[node]
        for i in arr:
            if visited[i]==0:
                counter += dfs(i,visited,counter)

    if counter!=0 and counter%2==0:
        result+=1
        print("#",node)
        counter=0
    
    return counter
    
    


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, d):
    root = 0
    visited=[0]*t_nodes
    counter=0
    a=dfs(root,visited,counter)
    


t_nodes, t_edges = map(int, input().rstrip().split())
result = 0
t_from = [0] * t_edges
t_to = [0] * t_edges
d={}
for i in range(t_edges):
    t_from, t_to = map(int, input().rstrip().split())
    t_from-=1
    t_to-=1
    if t_from not in d:
        d[t_from]=[t_to]
    else:
        d[t_from].append(t_to)

    if t_to not in d:
        d[t_to]=[t_from]
    else:
        d[t_to].append(t_from)

res = evenForest(t_nodes, t_edges, d)

print(result)
