import sys
N= int(sys.stdin.readline())


coins = list(map(int, sys.stdin.readline().split()))

M=int(sys.stdin.readline())

low, high = 0, max(coins)
result = 0

while low <= high:
    mid = (low + high) // 2
    sumcoin = 0
    for coin in coins:
        if coin>mid:
            sumcoin+=mid
        else:
            sumcoin+=coin

    if sumcoin <= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)