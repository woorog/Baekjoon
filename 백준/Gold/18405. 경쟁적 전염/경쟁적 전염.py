# 바이러스의 종류는 총 n 개 그럼 포문을 n 번 실행하고
# 그 포문을 실행할때 각자 종류순으로 bfs 실행 배열이 비어있으면 인접노드가
# 그 바이러스의 종류가되고 이전에 실행했던 부분은 visited 처리
# 마지막에 리스트를 참조해서 그 자리에 뭐가 있는지 출력해주면 끝

import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# N은 NxN 크기의 시험관
# M은 바이러스 종류
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

virusList = [[] for _ in range(M + 1)]

second, X, Y = map(int, input().split())

limitTime = second


def GetVirus():
    global limitTime
    time = 0

    que = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                virusList[graph[i][j]].append((graph[i][j],0, i, j))



    for i in range(1, len(virusList)):
        for pos in virusList[i]:
            que.append(pos)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        for _ in range(len(que)):

            val, time,x, y = que.popleft()
            if time == limitTime:
                break

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                    graph[nx][ny] = val
                    que.append((graph[nx][ny],time+1, nx, ny))




GetVirus()

print(graph[X - 1][Y - 1])

