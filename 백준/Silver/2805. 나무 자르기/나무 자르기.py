import sys
a = list(map(int, sys.stdin.readline().split()))

N=a[0]
M=a[1]

woods = list(map(int, sys.stdin.readline().split()))


low, high = 0, max(woods)
result = 0

while low <= high:
    mid = (low + high) // 2
    cut = 0
    for wood in woods:
        if wood > mid:
            cut += wood - mid


    if cut >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
