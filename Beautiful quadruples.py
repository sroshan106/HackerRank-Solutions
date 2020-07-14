def calc(a,b,c,d):
    a,b,c,d = sorted([a,b,c,d])
    #print(a,b,c,d)
    counter=0
    possible = 0
    pair = []
    for i in range(1,a+1):
        for j in range(i,b+1):
            pair.append([i,j])
            

    pair1=[]
    for k in range(1,c+1):
        for l in range(k,d+1):
            pair1.append([k,l])
            
    for i in range(len(pair)):
        x,y=pair[i][0],pair[i][1]
        
        for j in range(len(pair1)):
            p,q = pair1[j][0],pair1[j][1]
            if y<=p:
                #print([x,y,p,q],end =" ")
                if ((x^y)^(p^q))!=0:
                    possible+=1
                
    return(possible)
a,b,c,d = list(map(int,input().split(" ")))
print(calc(a,b,c,d))
