import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
nxt = []
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            nxt.append((x, y))

def check_h(x, a):
    # 가로줄 검증
    for y in range(9):
        if board[x][y] == a:
            return False
    return True

def check_v(y, a):
    # 세로줄 검증
    for x in range(9):
        if board[x][y] == a:
            return False
    return True

def check_b(x, y, a):
    # 네모 박스 검증
    x = x // 3 * 3
    y = y // 3 * 3
    for dx in range(x, x + 3):
        for dy in range(y, y + 3):
            if board[dx][dy] == a:
                return False
    return True

def sudoku(n):
    if n == len(nxt):
        for row in range(9):
            print(*board[row])
        sys.exit(0)
    x = nxt[n][0]
    y = nxt[n][1]
    for a in range(1, 10):
        if check_b(x, y, a) and check_h(x, a) and check_v(y, a):
            board[x][y] = a
            sudoku(n + 1)
            board[x][y] = 0


sudoku(0)
