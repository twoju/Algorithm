import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

q = deque()
box = []
visited = [[False] * (m) for _ in range(n)]
dist = [[0] * (m) for _ in range(n)]

for row in range(n):
    tomato = list(map(int, input().split()))
    box.append(tomato)
    for i in range(m):
        if tomato[i] == 1:
            q.append((row, i))
            visited[row][i] = True
        if tomato[i] == -1:
            visited[row][i] = True

if all(0 not in b for b in box):
    print(0)
    sys.exit(0)

while q:
    x, y = q.popleft()
    for dxy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx = x + dxy[0]
        dy = y + dxy[1]
        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if visited[dx][dy]:
            continue
        q.append((dx, dy))
        dist[dx][dy] = dist[x][y] + 1
        visited[dx][dy] = True

if all(False not in v for v in visited):
    print(max(map(max, dist)))
else:
    print(-1)