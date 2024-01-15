from itertools import *
import sys
num = []

for _ in range(9):
    num.append(int(sys.stdin.readline()))

printList = list(permutations(num, 7))
# print(printList)

for sumlist in printList:
    ans = []
    if sum(sumlist) == 100:
        ans = sorted(sumlist)
        for i in ans:
            print(i)
        break
