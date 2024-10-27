import copy

def maxblock(board):
    max_count = 0
    
    # 행 방향으로 연속된 같은 색 사탕 개수를 계산
    for i in range(len(board)):
        count = 1
        for j in range(1, len(board)):
            if board[i][j] == board[i][j - 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    
    # 열 방향으로 연속된 같은 색 사탕 개수를 계산
    for j in range(len(board)):
        count = 1
        for i in range(1, len(board)):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    
    return max_count

num = int(input())
board = [list(input().strip()) for _ in range(num)]
max_candies = 0

for i in range(num):
    for j in range(num):
        # 오른쪽 사탕과 교환
        if j + 1 < num and board[i][j] != board[i][j + 1]:
            temp = copy.deepcopy(board)
            temp[i][j], temp[i][j + 1] = temp[i][j + 1], temp[i][j]
            max_candies = max(max_candies, maxblock(temp))
        
        # 아래쪽 사탕과 교환
        if i + 1 < num and board[i][j] != board[i + 1][j]:
            temp = copy.deepcopy(board)
            temp[i][j], temp[i + 1][j] = temp[i + 1][j], temp[i][j]
            max_candies = max(max_candies, maxblock(temp))

print(max_candies)
