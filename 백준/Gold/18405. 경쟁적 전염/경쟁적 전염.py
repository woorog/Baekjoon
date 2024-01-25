from collections import deque

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 바이러스 초기 위치 및 종류 저장
virus_info = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus_info.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 위치(x, y)

# 바이러스 종류에 따라 정렬
virus_info.sort()

queue = deque(virus_info)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS 실행
while queue:
    virus, time, x, y = queue.popleft()

    if time == S:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, time + 1, nx, ny))

print(graph[X-1][Y-1])
