import sys
num = int(sys.stdin.readline())
a=num
ans=-1


cnt=0

while ans!=num:
    front=int(a/10)
    behind=a%10

    temp=front+behind

    ans=behind*10+(temp%10)

    cnt+=1
    a=ans
    

print(cnt)