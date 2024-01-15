import math
import sys

# a = list(map(int, sys.stdin.readline().split()))
# # a = [1, 2, 3, 4, 5]
#

# 여러 문장.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

# 앞으로의 코딩 입력 방식.


# listnum= list(map(int, sys.stdin.readline().split())) 한줄에 입력받는법
# listnum = [int(sys.stdin.readline().strip()) for _ in range(9)]   백준식 입력받기... 이게 하나씩됨
# num = int(sys.stdin.readline()) 한개만

# 골드바흐 시간 계산 모든 수를 계산하면 9996x9996 은 1억번이 안되기 떄문에 포문에 전체 탐색하는게 옳다고 가정하고 시작.
#
# 그렇다면 각 저장소에는 2개가 저장되게 되는데...
# 저장 할떄 두 소수의 차이가 가장작은 수를 저장하는 변수 하나 설정해서
# 그럼 절댓값을 세워서 값 차이를 저장하는 변수 하나
# 그리고 그 숫자보다 작은 소수를 저장 해 둬야함.

def move(no, x, y):

    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'{x} {y}')


    if no > 1:
        move(no - 1, 6 - x - y, y)


n = int(sys.stdin.readline())
x = 1
y = 3


if n>20:
    print(2**n-1) #이동횟수 출력
else:
    print(2**n-1) #이동횟수 출력
    move(n, x, y)



