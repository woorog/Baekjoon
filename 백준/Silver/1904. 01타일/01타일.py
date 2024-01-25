# 01 타일 문제를 풀때는 00 을 세트로 1 하나를 세트로 푼다고 생각을 하고

# 짝수면 00 의 경우 하나 추가.
# 1:1 2:2 3: 001 100 111(3) 4:0000 0011 1100 1001 1111(5) 5:00001 10000 00100 00111 10011 11001 11100 11111(8)
#그냥이거 피보나치아님?
import sys

a=int(sys.stdin.readline())

def pivo(k):

    prv2=1
    prv1=2
    now=0
    for _ in range(k-2):
        now=(prv1+prv2) % 15746
        prv2=prv1
        prv1=now
    return now

ans=pivo(a)

if a==1:
    print(1)
elif a==2:
    print(2)
else:
    print(ans)