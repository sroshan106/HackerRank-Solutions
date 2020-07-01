
import math
import os

def answerQuery(left, right):
    global s
    result = 0
    l=[0]*26
    odd = 0
    for i in range(left,right+1):
        l[ord(s[i-1])-ord('a')]+=1
    for  i in range(26):
        if l[i]%2==1:
            odd+=1
        result += l[i]//2
    
    result = math.factorial(result)
    for i in range(26):
        if l[i]!=0:
            result = result//(math.factorial(l[i]//2))
    if odd!=0:
        return int((result*odd)%1000000007)
    return int(result%1000000007)


s = input()

q = int(input().strip())

for _ in range(q):
    first_multiple_input = list(map(int,input().split(" ")))
    l = first_multiple_input[0]
    r = first_multiple_input[1]
    result = answerQuery(l, r)
    print(result)

