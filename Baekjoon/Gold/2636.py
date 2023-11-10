import sys
from collections import deque
input = sys.stdin.readline


def check():
    cnt = 0
    for i in range(col):
        for j in range(row):
            if board[i][j] == 1:
                cnt += 1
    return cnt

def bfs(x, y):
    visited = [[False] * row for _ in range(col)]
    q.append((x, y))
    visited[x][y] = True
    while q:
        cnt = 0
        x, y = q.popleft()
        for nxt in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx = x + nxt[0]
            dy = y + nxt[1]
            if dx < 0 or dy < 0 or dx >= col or dy >= row:
                continue
            if visited[dx][dy]:
                continue
            if board[dx][dy] == 0:
                q.append((dx, dy))
                visited[dx][dy] = True
            elif board[dx][dy] == 1:
                board[dx][dy] = 0
                visited[dx][dy] = True
            


col, row = map(int, input().split())

q = deque()
board = [list(map(int, input().split())) for _ in range(col)]

time = 0
ans = 0

while True:
    cheese = check()
    if cheese > 0:
        bfs(0, 0)
        time += 1
        ans = cheese
    elif cheese == 0:
        break

print(time)
print(ans)