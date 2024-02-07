import sys
input = sys.stdin.readline

sudoku = []
q = []
for x in range(9):
    s = list(map(int, input().split()))
    sudoku.append(s)
    for y in range(9):
        if s[y] == 0:
            q.append((x, y))

def row_col(n, row, col):
    # 가로 세로 줄 검증
    for i in sudoku[row]:
        if i == n:
            return False
    for i in range(9):
        if sudoku[i][col] == n:
            return False
    return True

def box(n, row, col):
    # 3으로 나눈 몫에 3을 곱하면 각 박스의 0번 인덱스 ~ +2 까지 확인 가능
    row = row // 3 * 3
    col = col // 3 * 3
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if sudoku[r][c] == n:
                return False
    return True

def recur(cur):
    if cur == len(q):
        for i in range(9):
            print(*sudoku[i])
        sys.exit(0)
    x, y = q[cur][0], q[cur][1]
    for i in range(1, 10):
        if row_col(i, x, y) and box(i, x, y):
            sudoku[x][y] = i
            recur(cur + 1)
            sudoku[x][y] = 0

recur(0)