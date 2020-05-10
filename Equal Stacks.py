#!/bin/python3

import os
#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    h1=h1[::-1]
    h2=h2[::-1]
    h3=h3[::-1]
    a=set()
    b=set()
    c=set()
    summ=0
    for i in h1:
        summ+=i
        a.add(summ)
    summ=0
    for i in h2:
        summ+=i
        b.add(summ)
    summ=0
    for i in h3:
        summ+=i
        c.add(summ)
    if (a&b&c): 
        return(max(a&b&c)) 
    else: 
        return("0")
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
