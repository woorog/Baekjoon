import sys
def gg(a, b, c):
    if b == 0:
        return 1

    half = gg(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

 # A^10은 (A^5) * (A^5)로 계산가능하다.
 #(x * y) % C는 ((x % C) * (y % C)) % C와 같음
A, B, C = list(map(int, sys.stdin.readline().split()))
result = gg(A, B, C)
print(result)