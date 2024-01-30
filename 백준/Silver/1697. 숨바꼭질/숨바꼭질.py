import sys
from collections import deque

S, E = (map(int, sys.stdin.readline().split()))


def bfs(S, E):
    if S >= E:  # 시작점이 종료점보다 크거나 같은 경우
        return S - E

    visited = [False] * (E * 2 + 1)
    q = deque()
    q.append(S)
    visited[S] = True
    cnt = 0

    while q:
        for _ in range(len(q)):
            x = q.popleft()

            if x == E:
                return cnt

            for nx in (x - 1, x + 1, x * 2):
                if 0 <= nx <= E * 2 and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)

        cnt += 1

    return cnt

# 예시 실행

print(bfs(S, E))  # 예상 출력: 4
