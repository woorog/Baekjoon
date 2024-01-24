import sys
from itertools import permutations, combinations, combinations_with_replacement

num,mix= (map(int, sys.stdin.readline().split()))
listnum=(map(int, sys.stdin.readline().split()))
nums=[]
for i in listnum:
    nums.append(i)

nums.sort()

a=permutations(nums,mix)
a=sorted(a)
for combo in a:
    print(' '.join(map(str, combo)))