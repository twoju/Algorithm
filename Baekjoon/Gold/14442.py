import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for _ in range(k + 1)]

q = deque()
# x, y, 부신 벽
q.append((0, 0, 0))
# 0 => 일반 방문, 1 => 벽부수고 방문
visited[0][0][0] = 1

while q:
    x, y, destroy = q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[destroy][n - 1][m - 1])
        sys.exit(0)

    for nxt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x + nxt[0], y + nxt[1]
        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue
        if board[dx][dy] == 1:
            if destroy >= k:
                continue
            if visited[destroy + 1][dx][dy] != -1:
                continue
            q.append((dx, dy, destroy + 1))
            visited[destroy + 1][dx][dy] = visited[destroy][x][y] + 1
        else:
            if visited[destroy][dx][dy] != -1:
                continue
            q.append((dx, dy, destroy))
            visited[destroy][dx][dy] = visited[destroy][x][y] + 1

print(-1)