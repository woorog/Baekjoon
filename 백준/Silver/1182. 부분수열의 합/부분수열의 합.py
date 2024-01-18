from itertools import  combinations
import sys

setnum= list(map(int, sys.stdin.readline().split()))
listnum= list(map(int, sys.stdin.readline().split()))

cnt=0

for i in range(setnum[0]):
    for combo in combinations(listnum, i+1):
        if len(combo)==0:
            continue
        if sum(combo)==setnum[1]:
            cnt+=1

print(cnt)
