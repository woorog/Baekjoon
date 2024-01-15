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


n = int(sys.stdin.readline())

pos = [0] * n
flag_a = [False] * n
flag_b = [False] * (2 * n - 1)  # 대각선 체크 배열의 크기 조정
flag_c = [False] * (2 * n - 1)
cnt = 0


def set(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n - 1]:  #모든방향 퀸 배치 체크
            pos[i] = j
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = True
            set(i + 1, n)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = False



set(0, n)
print(cnt)
# pos=[0]*8
#
# flag_a=[False] * 8#각 행에 퀸 배치 체크
# flag_b=[False] * 15 #대각선 왼쪽으로 퀸 배치 체크
# flag_c=[False] * 15#대각선 오른쪽으로 퀸 배치 체크
# cnt=0
# def put():
#
#     global cnt
#
#     for j in range(8):
#         for i in range(8):
#             print('1' if pos[i] == j else '0', end='')
#             if pos[i]==j:
#                 cnt +=1
#         print()
#
#
#
# def set(i:int):
#     for j in range(8):
#        if(not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+7]):    #모든방향 퀸 배치 체크
#             pos[i] =j #퀸을 j 행에 배치
#             if i==7: # 모든 열에 퀸 배치 완료.
#                 put()
#             else:
#                 flag_a[j]=flag_b[i+j] = flag_c[i-j+7] = True
#                 set(i+1)
#                 flag_a[j]=flag_b[i+j] = flag_c[i-j+7] = False
#
#
#
# set(0)
# print(cnt)

