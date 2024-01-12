import sys

def med3(a):

    if a>=90:
        return 'A'
    elif a>=80:
        return 'B'
    elif a>=70:
        return 'C'
    elif a>=60:
        return 'D'
    else:
        return 'F'



abclist= list(map(int, sys.stdin.readline().split()))

print(med3(*abclist))
