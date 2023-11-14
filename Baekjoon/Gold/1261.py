import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(dist[n - 1][m - 1])
        break
    for nxt in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx, dy = x + nxt[0], y + nxt[1]
        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue
        if visited[dx][dy]:
            continue
        if maze[dx][dy] == 1:
            dist[dx][dy] = dist[x][y] + 1
            q.append((dx, dy))
        else:
            dist[dx][dy] =  dist[x][y]
            q.appendleft((dx, dy))
        visited[dx][dy] = True