import sys
input = sys.stdin.readline
from collections import deque

def move(a, x, y):
    dx, dy = x, y
    while True:
        dx += dxy[a][0]
        dy += dxy[a][1]
        if board[dx][dy] == '#':
            dx -= dxy[a][0]
            dy -= dxy[a][1]
            break
        if board[dx][dy] == 'O':
            break
    return (dx, dy)

n, m = map(int, input().split())
board = []
x, y, x2, y2 = 0, 0, 0, 0

for i in range(n):
    arr = list(map(str, input().strip()))
    for j in range(m):
        if arr[j] == 'R':
            x, y = i, j
            arr[j] = '.'
        elif arr[j] == 'B':
            x2, y2 = i, j
            arr[j] = '.'
    board.append(arr)

visited = []
q = deque()
q.append([x, y, x2, y2, 0])
visited.append((x, y, x2, y2))

dxy = [(1, 0), (0, 1), (-1, 0),  (0, -1)]
ans = 11

while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt > 10:
        break
    if board[rx][ry] == 'O':
        ans = min(ans, cnt)
        break
    for i in range(4):
        rnx, rny = move(i, rx, ry)
        bnx, bny = move(i, bx, by)
        if board[bnx][bny] == 'O':
            continue
        if (rnx, rny) == (bnx, bny):
            if abs(rnx - rx) + abs(rny - ry) > abs(bnx - bx) + abs(bny - by):
                rnx -= dxy[i][0]
                rny -= dxy[i][1]
            else:
                bnx -= dxy[i][0]
                bny -= dxy[i][1]
        if (rnx, rny, bnx, bny) not in visited:
            q.append((rnx, rny, bnx, bny, cnt + 1))
            visited.append((rnx, rny, bnx, bny))
        

if ans == 11:
    print(-1)
else:
    print(ans)