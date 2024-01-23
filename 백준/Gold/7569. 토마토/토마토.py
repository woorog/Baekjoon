import sys
from collections import deque

def bfs_modified(box):
    queue = deque()
    visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    visited[i][j][k] = 0
                    queue.append((i, j, k))
                elif box[i][j][k] == -1:
                    visited[i][j][k] = 0
    while queue:
        z, y, x = queue.popleft()

        for direction in range(6):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nz = z + dz[direction]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and visited[nz][ny][nx] == -1:
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
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    isolated = True
                    for direction in range(6):
                        ni = i + dz[direction]
                        nj = j + dy[direction]
                        nk = k + dx[direction]
                        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and box[ni][nj][nk] != -1:
                            isolated = False
                            break
                    if isolated:
                        return True
    return False

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

if noway_modified(box):
    print(-1)
elif all0(box):
    print(0)
else:
    visited = bfs_modified(box)
    max_day = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == -1 and box[i][j][k] == 0:
                    print(-1)
                    sys.exit()
                max_day = max(max_day, visited[i][j][k])
    
    print(max_day)
