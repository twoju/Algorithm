import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for _ in range(2)]

q = deque()
# x, y, 부신 벽
q.append((0, 0, 0))
# 0 => 일반 방문, 1 => 벽부수고 방문
visited[0][0][0], visited[1][0][0] = 1, 1
isRoute = False

while q:
    x, y, destroy = q.popleft()
    if x == n - 1 and y == m - 1:
        isRoute = True
        break
    if destroy > 1:
        continue
    for nxt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x + nxt[0], y + nxt[1]
        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue
        if visited[destroy][dx][dy] != -1:
            continue
        if board[dx][dy] == 1:
            q.append((dx, dy, destroy + 1))
            visited[1][dx][dy] = visited[0][x][y] + 1
        else:
            q.append((dx, dy, destroy))
            visited[destroy][dx][dy] = visited[destroy][x][y] + 1

if isRoute:
    print(max(visited[0][n - 1][m - 1], visited[1][n - 1][m - 1]))
else:
    print(-1)