import heapq
import sys
def max_heap_operations(ops):
    heap = []
    result = []

    for op in ops:
        if op == 0:
            if heap:
                # 최대값 추출 (실제로는 최소 힙에서 최소값을 추출하고, 부호를 바꿈)
                result.append(-heapq.heappop(heap))
            else:
                # 힙이 비어 있으면 0 출력
                result.append(0)
        else:
            # 새 요소를 최소 힙에 추가 (부호를 바꿔서 최대 힙처럼 동작하게 함)
            heapq.heappush(heap, -op)

    return result

N = int(sys.stdin.readline())
ops =[int(sys.stdin.readline())for i in range(N)]

results = max_heap_operations(ops)
for res in results:
    print(res)