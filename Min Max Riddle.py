
def riddle(arr):
    length =len(arr)
    d = [0]*(length)
    res=[]
    result =[]

    for i in range(length):
        result.append(d)
    res.append(max(arr))
    result[0]= arr;
    for i in range(1,length):
        for j in range(length-1):
            result[i][j]=min(result[i-1][j],result[i-1][j+1])
        res.append(max(result[i]))
    
    return res;

n = int(input())

arr = list(map(int, input().rstrip().split()))

res = riddle(arr)
for i in res:
    print(i,end=" ")
