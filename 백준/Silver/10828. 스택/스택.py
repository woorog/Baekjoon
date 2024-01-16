import sys
num= int(sys.stdin.readline())
stack=[]

for i in range(num):
    temp = sys.stdin.readline().split()
    if temp[0]=='push':
        stack.append(temp[1])
    elif temp[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif temp[0] == 'size':
        print(len(stack))
    elif temp[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif temp[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
