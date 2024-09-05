def count_unique_substrings(s):
    substrings = set()  # 중복을 제거하기 위한 집합
    n = len(s)
    
    # 모든 부분 문자열을 집합에 추가
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])
    
    return len(substrings)

# 입력 받기
S = input().strip()
print(count_unique_substrings(S))
