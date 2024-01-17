def matrix_mult(A, B, mod):
    """ 두 행렬 A와 B를 곱하고, 모든 원소를 mod로 나눈 결과를 반환합니다. """
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def matrix_power(A, n, mod):
    """ 행렬 A의 n 제곱을 계산합니다. """
    size = len(A)
    # 단위 행렬 생성
    result = [[1 if i == j else 0 for i in range(size)] for j in range(size)]
    while n > 0:
        if n % 2:
            result = matrix_mult(result, A, mod)
        A = matrix_mult(A, A, mod)
        n //= 2
    return result

def read_matrix(size):
    """ 행렬을 읽어들입니다. """
    return [list(map(int, input().split())) for _ in range(size)]

def print_matrix(A):
    """ 행렬을 출력합니다. """
    for row in A:
        print(' '.join(map(str, row)))

N, B = map(int, input().split())
mod = 1000
A = read_matrix(N)

result = matrix_power(A, B, mod)
print_matrix(result)
