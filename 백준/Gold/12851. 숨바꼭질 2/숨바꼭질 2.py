import sys
from collections import deque

S, E = (map(int, sys.stdin.readline().split()))
def find_fastest_path(N, K):
    if N >= K:
        return N - K, 1  # 수빈이가 동생보다 앞에 있거나 같은 위치에 있을 때

    visited = [0] * 100001  # 방문 여부와 해당 위치에 도달하는 최소 시간 기록
    ways = [0] * 100001  # 각 위치에 도달하는 방법의 수
    q = deque()
    q.append(N)
    visited[N] = 1  # 시작 위치 방문 처리
    ways[N] = 1  # 시작 위치 도달 방법은 1가지

    while q:
        x = q.popleft()

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000:
                if visited[nx] == 0:  # 처음 방문하는 경우
                    visited[nx] = visited[x] + 1
                    ways[nx] = ways[x]
                    q.append(nx)
                elif visited[nx] == visited[x] + 1:  # 이미 방문했지만, 최소 시간으로 도달하는 경우
                    ways[nx] += ways[x]

    return visited[K] - 1, ways[K]  # 시작 위치의 시간이 1로 계산되었으므로 -1

# 예시 입력

fastest_time, num_ways = find_fastest_path(S, E)
print(fastest_time)  # 가장 빠른 시간
print(num_ways)      # 방법의 수


# x=q.popleft()
# print(x)
#
# if 2*x==E or x-1==E or x+1==E:
#     cnt+=1
#     print('b')
#     break
# print( vistied[2*x])
# if vistied[2*x]==0 and 2*x<E+1:
#     vistied[2*x]=1
#     q.append(2*x)
#
# if vistied[x+1]==0 and x+1<E:
#     q.append(x+1)
#     vistied[x+1]=1
#
# if vistied[x-1]==0 and x-1<E:
#     q.append(x-1)
#     vistied[2*1]=1
#
# cnt+=1

#원래 코드랑 다른점은 큐를 다 뽑아서 카운트