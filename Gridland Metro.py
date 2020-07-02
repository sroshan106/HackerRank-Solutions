
def gridlandMetro(n, m, k, track):
    if k==0:
        return m*n
    visited=[0]*n
    arr = [0]*m
    counter = 0
    prev = track[0][0]
    for i in range(k):
        r,c1,c2 = track[i]
        if prev!=r:
            visited[prev-1]=1    
            counter+= arr.count(0)
            arr=[0]*m
        for p in range(c1-1,c2):
            arr[p]=1
        prev=r


    visited[r-1]=1   
    counter+= arr.count(0)
    temp = visited.count(0)
    
    counter+=temp*m
    return counter

        
nmk = input().split()

n = int(nmk[0])

m = int(nmk[1])

k = int(nmk[2])

track = []

for _ in range(k):
    track.append(list(map(int, input().rstrip().split())))

result = gridlandMetro(n, m, k, track)
print(result)
