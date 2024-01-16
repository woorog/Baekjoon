import sys
from collections import deque
# 보드 크기와 사과 위치 입력

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = set(tuple(map(int, sys.stdin.readline().split())) for _ in range(k))

# 방향 전환 정보 입력
l = int(sys.stdin.readline())
direction_changes = dict(sys.stdin.readline().split() for _ in range(l))

# 초기 설정
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
current_direction = 0  # 처음에는 동쪽을 바라보고 있음
snake = deque([(1, 1)])  # 뱀의 초기 위치
time = 0

def turn(direction, c):
    if c == "L":
        return (direction - 1) % 4  #0은 동쪽, 1은 남쪽, 2는 서쪽, 3은 북쪽을 그러니 -1 뺴면 동쪽에서 왼쪽으로 회전하면 북쪽임.
    else:
        return (direction + 1) % 4


while True:
    time += 1
    head_y, head_x = snake[0]
    dy, dx = directions[current_direction]
    new_head_y, new_head_x = head_y + dy, head_x + dx

    # 벽이나 자기 자신과 부딪히면 게임 종료
    if not (1 <= new_head_y <= n and 1 <= new_head_x <= n) or (new_head_y, new_head_x) in snake:
        break

    # 사과를 먹으면 길이가 늘어남
    if (new_head_y, new_head_x) in apples:
        apples.remove((new_head_y, new_head_x))
    else:
        snake.pop()  # 사과가 없으면 꼬리를 줄임

    snake.appendleft((new_head_y, new_head_x))  # 머리 이동

    # 방향 전환
    if str(time) in direction_changes:
        current_direction = turn(current_direction, direction_changes[str(time)])

print(time)

#현재 뱀 몸통은 큐로 구현하고 사과를 먹었으면 큐에 넣기만 하고 뺴지 않게 만들면 되고
#사과를 먹지 않았으면 큐에서 빼고 이동경로에 추가 이때 벽에 부딪히거나 자신의 몸통에 박으면 게임 셋
#           #그니까 여기서 보드 1에 만나면 지렁이 길이는 길어지고 1은 0 이됨
#             #자신의 몸과 벽을 박으면 게임이 끝나도록 설계하면 됨.
#             #현재 포인터가 가르키는 위치 갱신만 잘되면 쉬울듯.
