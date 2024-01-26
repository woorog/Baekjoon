N, M = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (M + 1)

for coin, cost in bags:
    for i in range(M, coin - 1, -1):
        dp[i] = max(dp[i], dp[i - coin] + cost)

print(max(dp))