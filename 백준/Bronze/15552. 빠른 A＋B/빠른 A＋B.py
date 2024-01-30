import sys

# num,tc=map(int, sys.stdin.readline().split())
# numlist=list(map(int, sys.stdin.readline().split()))
#
# for _ in range(tc):
#     sum=0
#     S,E=(map(int, sys.stdin.readline().split()))
#
#     for i in range(S-1,E):
#         sum=numlist[i]+sum
#
#     print(sum)\


n=int(sys.stdin.readline())

for _ in range(n):
    S,E=(map(int, sys.stdin.readline().split()))
    print(S+E)