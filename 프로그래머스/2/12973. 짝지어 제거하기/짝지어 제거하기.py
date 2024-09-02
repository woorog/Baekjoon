def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 현재 문자와 스택의 마지막 문자가 같다면 제거
        else:
            stack.append(char)  # 그렇지 않으면 스택에 추가
    
    # 스택이 비어있다면 모든 짝을 제거한 것이므로 1, 그렇지 않으면 0 반환
    return 1 if not stack else 0
