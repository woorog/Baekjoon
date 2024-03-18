import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(y, x, num):
    # Check row
    if num in board[y]:
        return False
    # Check column
    if num in [board[i][x] for i in range(9)]:
        return False
    # Check subgrid
    start_row, start_col = 3 * (y // 3), 3 * (x // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku():
    if not empty_cells:
        return True

    y, x = empty_cells[0]
    for num in range(1, 10):
        if is_valid(y, x, num):
            board[y][x] = num
            empty_cells.pop(0)
            if solve_sudoku():
                return True
            board[y][x] = 0
            empty_cells.insert(0, (y, x))
    return False

solve_sudoku()

for row in board:
    print(*row)
