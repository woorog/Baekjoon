
import heapq
import sys
def find_medians(nums):
    max_heap = []  # 작은 값들을 저장하는 최대 힙 (Python에서는 최소 힙으로 구현하므로, 값에 -1을 곱함)
    min_heap = []  # 큰 값들을 저장하는 최소 힙
    result = []

    for num in nums:
        if not max_heap or -max_heap[0] >= num:
            heapq.heappush(max_heap, -num)  # 최대 힙에 값 추가
        else:
            heapq.heappush(min_heap, num)  # 최소 힙에 값 추가

        # 두 힙의 크기를 조절하여 중간값을 최대 힙의 루트에 유지
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중간값을 결과 리스트에 추가
        result.append(-max_heap[0])

    return result

N = int(sys.stdin.readline())
nums =[int(sys.stdin.readline().strip()) for _ in range(N)]
medians = find_medians(nums)

for median in medians:
    print(median)

