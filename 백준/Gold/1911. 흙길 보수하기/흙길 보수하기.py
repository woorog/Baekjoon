# import math
# import sys
#
# tc,lens=map(int,sys.stdin.readline().split())
#
# waters=[]
# for _ in range(tc):
#     a,b=map(int,sys.stdin.readline().split())
#     waters.append((a,b))
#
# waters.sort()
#
#
# start,end=waters[0][0],waters[0][1]
# sums=0
# for i in range(1,tc):
#     ns,ne=waters[i][0],waters[i][1]
#
#     temp=(end-start)%lens
#     prov=end-temp+lens
#
#     if prov<ns+1:
#         sums+= math.ceil((end-start)/lens)
#         start=ns
#         end=ne
#     elif ne>end:
#         end=ne
#
# sums+= math.ceil((end-start)/lens)
#
# print(sums)
#
import math
import sys

N,L=map(int,sys.stdin.readline().split())

waters=[]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    waters.append((a,b))

# 웅덩이들을 시작 위치를 기준으로 정렬
waters.sort()

# 널빤지 필요 개수와 현재 널빤지의 끝 위치 초기화
planks_needed = 0
current_end = 0

for start, end in waters:
    # 현재 널빤지가 물웅덩이를 덮지 못하는 경우
    if start > current_end:
        # 새로운 널빤지를 사용해야 함
        planks_needed += math.ceil((end - start) / L)
        current_end = start + math.ceil((end - start) / L) * L
    else:
        # 현재 널빤지로 덮을 수 있는 경우, 필요한 경우에만 널빤지 추가
        if end > current_end:
            planks_needed += math.ceil((end - current_end) / L)
            current_end = current_end + math.ceil((end - current_end) / L) * L

print(planks_needed)
