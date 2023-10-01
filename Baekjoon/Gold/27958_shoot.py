def split_point(r, c):
    global board
    for i in range(4):
        x = (r + dx[i]) % n
        y = (c + dy[i]) % n
        if board[x][y] == 0:
            board[x][y] = board[r][c] // 4


n = int(input())
k = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
turn = 0

attack = list(map(int, input().split()))
select = -1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while True:
    if turn == k:
        break
    max_bonus = 0
    for i in range(n):
        if board[i][turn] > max_bonus:
            max_bonus = board[i][turn]
            select = i
    if max_bonus >= 10:
        ans += max_bonus
        split_point(select, turn)
    else:
        if board[select][turn] > attack[turn]:
            board[select][turn] -= attack[turn]
        else:
            ans += board[select][turn]
            board[select][turn] = 0

print(ans)