import sys

tc=int(sys.stdin.readline())
arr=[]
for i in range(tc):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp=[[0]*(tc+1) for i in range(tc+1)]

dp[0][0]=arr[0][0]

for i in range(tc):
    cnt=0
    for k in arr[i]:
        if i+1<tc and dp[i][cnt]+arr[i+1][cnt]>dp[i+1][cnt] :
            dp[i+1][cnt]=dp[i][cnt]+arr[i+1][cnt]

        if i+1<tc and dp[i][cnt]+arr[i+1][cnt+1]>dp[i+1][cnt+1]:
            dp[i+1][cnt+1]=dp[i][cnt]+arr[i+1][cnt+1]
        cnt+=1





print(max(dp[tc-1]))
