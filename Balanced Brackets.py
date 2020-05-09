

def isBalanced(s):
    stack1=[]
    for i in range(len(s)):
        if(s[i]=='{' or s[i]=='(' or s[i]=='['):
            stack1.append(s[i])
        elif(s[i]=='}' or s[i]==']' or s[i]==')'):
            if(stack1==[]):
                return 'NO'
            if(s[i]==')' and stack1.pop()!='('):
                return 'NO'
            if(s[i]==']' and stack1.pop()!='['):
                return 'NO'
            if(s[i]=='}' and stack1.pop()!='{'):
                return 'NO'
    if(stack1==[]):
        return 'YES'
    else:
        return 'NO'


t = int(input())

for t_itr in range(t):
    s = input()

    result = isBalanced(s)
    print(result)
