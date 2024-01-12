import sys


# a = list(map(int, sys.stdin.readline().split()))
# # a = [1, 2, 3, 4, 5]
#

# 여러 문장.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

# 앞으로의 코딩 입력 방식.



num= list(map(int, sys.stdin.readline().split()))

for i in range(1,10):

    print(f"{int(*num)} * {i} =",int(*num) * i,end='\n')


