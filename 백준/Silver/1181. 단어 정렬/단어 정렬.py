import sys
n = int(sys.stdin.readline())
num = []
num_set=[]
for _ in range(n):
    num.append(str(sys.stdin.readline()))


num_set=set(num)
# print(num_set)
num=list(num_set)
num.sort()  #사전순 정렬 해주고
num.sort(key=lambda x:len(x)) # 길이순 정렬 이거 몰라서 못풀었으니 기억할것.

for i in num:
    print(i,end='')