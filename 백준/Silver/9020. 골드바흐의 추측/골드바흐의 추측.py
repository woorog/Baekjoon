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


N = int(sys.stdin.readline())

def prime(N): # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

for _ in range(N):
    num = int(sys.stdin.readline())

    tempa = num // 2 # 두 수 중 줄어드는 변수
    tempb = num // 2 # 두 수 중 늘어나는 변수

    for _ in range(num // 2):
        if prime(tempa) and prime(tempb): # 둘다 소수이면 출력
            print(tempa, tempb)
            break
        else: # 소수가 아니면 줄이고 늘리기
            tempa -= 1
            tempb += 1




