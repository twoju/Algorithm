import sys
from collections import deque

# 일단 냅다 최단 거리로 가는 방법을 찾고
# 1인 경우를 카운트해서
# 2가 넘으면 바로 컷

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * (m + 1) for _ in range(n + 1)]
dist = [[0] * (m + 1) for _ in range(n + 1)]

q = deque()
q.append((1, 1))
visited[1][1] = True
dist[1][1] = 1
isRoute = False

while q:
    x, y = q.popleft()
    if x == n and y == m:
        isRoute = True
        break
    wall = 0
    for nxt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x + nxt[0], y + nxt[1]
        if dx < 1 or dy < 1 or dx > n or dy > m:
            continue
        if visited[dx][dy]:
            continue
        if board[dx - 1][dy - 1] == 1:
            if wall > 1:
                continue
            wall += 1
        q.append((dx, dy))
        visited[dx][dy] = True
        dist[dx][dy] = dist[x][y] + 1

if isRoute:
    print(dist)
    print(dist[n][m] + 1)
else:
    print(-1)