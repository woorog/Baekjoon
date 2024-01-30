import sys

input = sys.stdin.readline

n = int(input())

dp = [[1]*10 for _ in range(n)]
dp[0][0] = 0

for j in range(1,n):
    for i in range(10):
        if i == 0 : 
            dp[j][i] = dp[j-1][i+1]
        elif i == 9:
            dp[j][i] = dp[j-1][i-1]
        else :
            dp[j][i] = dp[j-1][i+1] + dp[j-1][i-1]

print(sum(dp[n-1])%1000000000)