import sys
from itertools import permutations, combinations, combinations_with_replacement

num,mix= (map(int, sys.stdin.readline().split()))
nums=[]
for i in range(num):
    nums.append(i+1)


a=combinations_with_replacement(nums,mix)

for combo in a:
    print(' '.join(map(str, combo)))