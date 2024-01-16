import sys
N = int(sys.stdin.readline())  # 탑의 수
towers =list(map(int, sys.stdin.readline().split()))  # 탑들의 높이

stack = []  # 탑의 인덱스를 저장할 스택
result = [0] * N  # 결과를 저장할 리스트

for i, height in enumerate(towers):
    # 스택이 비어 있지 않고, 현재 탑의 높이가 스택의 탑 높이보다 클 때까지 스택에서 탑을 제거
    while stack and towers[stack[-1]] < height:
        stack.pop()

    # 스택이 비어 있지 않으면 현재 탑은 스택의 최상단 탑에서 레이저를 수신
    if stack:
        result[i] = stack[-1] + 1  # 인덱스는 0부터 시작하므로 +1

    # 현재 탑 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(' '.join(map(str, result)))
