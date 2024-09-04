def solve_board(board):
    # '.'로 구분하여 각 구간을 처리
    parts = board.split('.')
    
    for i in range(len(parts)):
        length = len(parts[i])
        
        # X의 길이에 따라 처리
        if length % 2 != 0:  # 홀수인 경우 덮을 수 없음
            return -1
        
        # 최대한 AAAA를 먼저 채운다
        parts[i] = 'AAAA' * (length // 4) + 'BB' * ((length % 4) // 2)
    
    # 각 부분을 '.'를 기준으로 다시 합침
    return '.'.join(parts)

# 입력
board = input().strip()

# 출력
result = solve_board(board)
print(result)
