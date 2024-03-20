import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for nxt in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            dx, dy = x + nxt[0], y + nxt[1]
            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                continue
            if board[dx][dy] == 0:
                continue
            if dist[dx][dy] == -1:
                q.append((dx, dy))
                dist[dx][dy] = dist[x][y] + 1

n, m = map(int, input().split())
board = []
dist = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 0:
            dist[i][j] = 0
        if arr[j] == 2:
            q.append((i, j))
            dist[i][j] = 0
    board.append(arr)


bfs()

for arr in dist:
    print(*arr)