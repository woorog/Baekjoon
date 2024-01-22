import sys
from collections import deque


def bfs(k, coins):
    queue = deque()
    queue.append((0, 0))  # (현재 금액, 사용한 동전 수)
    visited = set()  # 방문한 금액 추적

    while queue:
        current_sum, coin_count = queue.popleft()

        if current_sum == k:
            return coin_count

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum <= k and next_sum not in visited:
                queue.append((next_sum, coin_count + 1))
                visited.add(next_sum)

    return -1  # 목표 금액을 만들 수 없는 경우


N=list(map(int, sys.stdin.readline().split()))
coins=[int(sys.stdin.readline().strip()) for _ in range(N[0])]


print(bfs(N[1], coins))
