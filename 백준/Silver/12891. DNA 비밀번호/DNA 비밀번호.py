lendna, lenpass = map(int, input().split())
dna = list(input().strip())
a, c, g, t = map(int, input().split())

# 초기 윈도우 설정
start = 0
end = lenpass
na = nc = ng = nt = 0
ans = 0

# 초기 윈도우에서의 A, C, G, T 개수 세기
for i in range(lenpass):
    if dna[i] == 'A':
        na += 1
    elif dna[i] == 'C':
        nc += 1
    elif dna[i] == 'G':
        ng += 1
    elif dna[i] == 'T':
        nt += 1

# 첫 번째 윈도우가 조건을 만족하는지 확인
if na >= a and nc >= c and ng >= g and nt >= t:
    ans += 1

# 슬라이딩 윈도우로 전체 문자열 탐색
for i in range(1, lendna - lenpass + 1):
    # 윈도우의 첫 번째 문자를 빼고, 다음 문자를 추가
    if dna[i - 1] == 'A':
        na -= 1
    elif dna[i - 1] == 'C':
        nc -= 1
    elif dna[i - 1] == 'G':
        ng -= 1
    elif dna[i - 1] == 'T':
        nt -= 1

    if dna[i + lenpass - 1] == 'A':
        na += 1
    elif dna[i + lenpass - 1] == 'C':
        nc += 1
    elif dna[i + lenpass - 1] == 'G':
        ng += 1
    elif dna[i + lenpass - 1] == 'T':
        nt += 1

    # 현재 윈도우가 조건을 만족하는지 확인
    if na >= a and nc >= c and ng >= g and nt >= t:
        ans += 1

# 결과 출력
print(ans)