import sys


num = int(sys.stdin.readline())

for i in range(num):

    lists= list(map(str, sys.stdin.readline().split()))
    # print(lists)
    alpabet=list(lists[1])
    for k in range(len(alpabet)):
        print(alpabet[k]*int(lists[0]),end='')
    print()



