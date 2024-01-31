import sys

num=int(sys.stdin.readline())
numlist=list(map(int, sys.stdin.readline().split()))
numlist.append(-99999999)
ans=numlist[0]
dp=[numlist[0]]
for i in range(1,num):

    now=numlist[i]
    if now>ans:
        ans=now
    cnt=0

    for k in dp:
        dp[cnt]=dp[cnt]+now
        cnt+=1
        if ans<max(dp):
            ans=max(dp)

    if max(dp)<now:
        dp[0]=now




print(ans)
