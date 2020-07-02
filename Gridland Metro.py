
def gridlandMetro(n, m, k, track):
    if k==0:
        return m*n
    d={}
    counter = m*n
    for i in range(k):
        r,c1,c2 = track[i]
        if r not in d:
            d[r]=[c1,c2]
        else:
            left,right = d[r]
            if left>c1:
                left = min(left,c1)
            if right<c2:
                if c1>right:
                    counter+=c1-right-1
                right = max(right,c2)
            d[r]=[left,right]
    for i,j in d.values():
        counter = counter - (j-i+1)
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
