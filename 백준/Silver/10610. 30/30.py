num = input()

# 조건 1: 숫자에 0이 포함되어 있어야 30의 배수를 만들 수 있음
if '0' not in num:
    print(-1)
else:
    # 조건 2: 각 자리 숫자의 합이 3의 배수여야 함
    if sum(map(int, num)) % 3 != 0:
        print(-1)
    else:
        # 30의 배수를 만들 수 있으므로, 내림차순으로 정렬하여 가장 큰 수를 출력
        print(''.join(sorted(num, reverse=True)))