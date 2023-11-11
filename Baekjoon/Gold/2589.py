import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())
board = [list(input().strip()) for _ in range(col)]
cnt = 0

for i in range (col):
    for j in range(row):
        if board[i][j] == 'L':
            q = deque()
            visited = [[False] * row for _ in range(col)]
            dist = [[0] * row for _ in range(col)]
            q.append((i, j))
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                for nxt in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dx, dy = x + nxt[0], y + nxt[1]
                    if dx < 0 or dy < 0 or dx >= col or dy >= row:
                        continue
                    if board[dx][dy] == 'W':
                        continue
                    if visited[dx][dy]:
                        continue
                    q.append((dx, dy))
                    visited[dx][dy] = True
                    dist[dx][dy] = dist[x][y] + 1

            for arr in dist:
                cnt = max(cnt, max(arr))

print(cnt)