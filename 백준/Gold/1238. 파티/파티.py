import copy
import heapq
import sys
from collections import deque


class Graph:
    def __init__(self, num):
        self.graph = {i: [] for i in range(1, num + 1)}


    def add_edge(self,u,v,cost):
        self.graph[u].append((v,cost))





def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex] < current_distance:
            continue

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


N,tc,point=list(map(int,sys.stdin.readline().split()))
g=Graph(N)
edges=[]
for _ in range(tc):
    edges.append(list(map(int,sys.stdin.readline().split())))



graph = Graph(N)
for u, v, w in edges:
    graph.add_edge(u, v, w)

# 역방향 그래프 초기화 및 간선 추가
reverse_graph = Graph(N)
for u, v, w in edges:
    reverse_graph.add_edge(v, u, w)

# 각 정점에서 X로 가는 최단 경로
distances_to_X = dijkstra(graph, point)

# X에서 각 정점으로 돌아오는 최단 경로
distances_from_X = dijkstra(reverse_graph, point)

# 각 학생의 오고 가는데 걸리는 최대 시간 계산
max_time = 0
for node in graph.graph:
    time = distances_to_X[node] + distances_from_X[node]
    max_time = max(max_time, time)

print(max_time)

