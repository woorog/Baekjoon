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


#
# def shaker_sort(a):
#     n = len(a)
#     swapped = True
#     start = 0
#     end = n - 1
#     while swapped:
#         swapped = False
#         for i in range(start, end):
#             if a[i] > a[i + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#                 swapped = True
#         if not swapped:
#             break
#         swapped = False
#         end -= 1
#         for i in range(end - 1, start - 1, -1):
#             if a[i] > a[i + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#                 swapped = True
#         start += 1
# def binary_sort(a):
#     for i in range(1, len(a)):
#         key = a[i]
#         left = 0
#         right = i
#         while left < right:
#             mid = (left + right) // 2
#             if a[mid] > key:
#                 right = mid
#             else:
#                 left = mid + 1
#         for j in range(i, left, -1):
#             a[j] = a[j - 1]
#         a[left] = key
#
# n = int(sys.stdin.readline())
# a = [int(sys.stdin.readline()) for _ in range(n)]
# binary_sort(a)
# for num in a:
#     print(num)

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)