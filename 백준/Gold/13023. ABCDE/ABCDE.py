import sys

node, tc = map(int, input().split())
dic = {i: [] for i in range(node)}  # 모든 노드를 키로 하는 딕셔너리 초기화

for _ in range(tc):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

def dfs(now, depth, visited):
    if depth == 4:
        return True
    visited[now] = True
    for next_node in dic[now]:  # 여기서 KeyError가 발생하지 않도록 모든 키를 초기화
        if not visited[next_node]:
            if dfs(next_node, depth + 1, visited):
                return True
    visited[now] = False
    return False

result = False
for i in range(node):
    visited = [False] * node
    if dfs(i, 0, visited):
        result = True
        break

print(1 if result else 0)
