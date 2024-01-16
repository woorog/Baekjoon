import sys
def josephus_permutation(n, k):
    sequence = list(range(1, n + 1))
    result = []
    index = 0

    while sequence:
        index = (index + k - 1) % len(sequence)
        result.append(sequence.pop(index))

    return result

# 예제 입력
listnum= list(map(int, sys.stdin.readline().split()))
n, k = listnum[0],listnum[1]

josephus_sequence = josephus_permutation(n, k)
print(f'<',end='')
for i in range(n):
    if i<n-1:
        print(f'{josephus_sequence[i]}, ',end='')
    else:
        print(f'{josephus_sequence[i]}',end='')
print(f'>',end='')