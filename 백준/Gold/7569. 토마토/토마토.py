import sys
from collections import deque


def bfs_modified(box):
    queue = deque()
    visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
    for i in range(H):
        for l in range(N):
            for k in range(M):
                if box[i][l][k] == 1:
                    visited[i][l][k] = 0
                    queue.append((i, l, k))
                elif box[i][l][k] == -1:
                    visited[i][l][k] = 0
    while queue:
        z, y, x = queue.popleft()

        for direction in range(6):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nz = z + dz[direction]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == -1:
                queue.append((nz, ny, nx))
                visited[nz][ny][nx] = visited[z][y][x] + 1

    return visited
def all0(box):
    for layer in box:
        for row in layer:
            if any(cell == 0 for cell in row):
                return False
    return True

def noway_modified(box):
    for i in range(H):
        for l in range(N):
            for k in range(M):
                if box[i][l][k] == 0:
                    isolated = True
                    for direction in range(6):
                        ni = i + dz[direction]
                        nl = l + dy[direction]
                        nk = k + dx[direction]
                        if 0 <= ni < H and 0 <= nl < N and 0 <= nk < M and box[ni][nl][nk] != -1:
                            isolated = False
                            break
                    if isolated:
                        return True
    return False

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 높이 H, 행 M, 열 N을 입력받습니다.
M, N, H = map(int, input().split())
#M, N, H = (map(int, sys.stdin.readline().split()))
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]




if noway_modified(box):
    print(-1)
elif all0(box):
    print(0)
else:
    visited = bfs_modified(box)
    max_day = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == -1 and box[i][j][k] == 0:
                    print(-1)
                    sys.exit()
                max_day = max(max_day, visited[i][j][k])

    print(max_day)