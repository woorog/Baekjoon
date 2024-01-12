import sys


num = int(sys.stdin.readline())
listnum= list(map(int, sys.stdin.readline().split()))
sum=0;

for i in range(num):
    if listnum[i]==1:
        sum+=1
        continue
    else:
        for k in range(2,listnum[i]):
            if listnum[i]%k==0:
                sum+=1
                
                break


print(num-sum)

