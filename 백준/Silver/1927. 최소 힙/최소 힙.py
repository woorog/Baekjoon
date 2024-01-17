from heapq import *
import sys
import heapq
num = int(sys.stdin.readline())
listnum = [int(sys.stdin.readline().strip()) for _ in range(num)]
heap=[]

for i in range(num):
    if listnum[i]==0:
        if len(heap)==0:
            print(0)
        else:
            smallest = heapq.heappop(heap)
            print(smallest)
    else:
        heappush(heap,listnum[i])



