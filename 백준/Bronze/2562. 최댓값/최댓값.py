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

listnum = [int(sys.stdin.readline().strip()) for _ in range(9)]
max=0
T=0


for i in range(len(listnum)):
    if listnum[i]>T:
        max=i
        T=listnum[i]



print(listnum[max])
print(max+1)
