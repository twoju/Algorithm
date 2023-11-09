import sys
from collections import deque

n, m = map(int, input().split())

maze = [[0] * (m) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
dist = [[0] * (m) for _ in range(n)]

for row in range(n):
    arr = list(map(int, input()))
    for col in range(m):
        maze[row][col] = arr[col]
        if arr[col] == 0:
            visited[row][col] = True

dist[0][0] = 1
visited[0][0] = True

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(dist[n - 1][m - 1])
        break
    for nxt in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx = x + nxt[0]
        dy = y + nxt[1]
        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if visited[dx][dy]:
            continue
        q.append((dx, dy))
        visited[dx][dy] = True
        dist[dx][dy] = dist[x][y] + 1
