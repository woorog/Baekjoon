import sys 
num = int(sys.stdin.readline())
array = [[0 for col in range(num)] for row in range(num)]
ans=sys.maxsize
visited=[0]*num

for j in range(num):
    array[j]= list(map(int, sys.stdin.readline().split()))

def loopf(start,now,value,deep):
    global ans
    #n-1 번까지 완전 탐색했을때 n 번째에 start번 선택지로 가는 것이 무조건 선택 되어야만 한다.
    if deep==num:
        if array[now][start]:
            value += array[now][start]
            if ans > value:
                ans = value
        return
    if value > ans:  #만약 값이 최소값보다 클땐 그냥 스킵
        return
    #일반적으론 함수 실행.
    for i in range(num):
        if not visited[i] and array[now][i]:
            visited[i] = 1
            loopf(start, i, value + array[now][i], deep + 1)
            visited[i] = 0

#모든 시작점 검색
for i in range(num):
    visited[i] = 1
    loopf(i,i,0,1)
    visited[i] = 0
print(ans)
