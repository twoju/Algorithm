import sys
input = sys.stdin.readline 
from collections import deque

n, m = map(int, input().split())
board = []
start = []
for i in range(n):
    arr = list(input().strip())
    for j in range(m):
        if arr[j] == 'L':
            start.append((i, j))
    board.append(arr)

ans = 0
for i in range(len(start)):
    q = deque()
    q.append(start[i])
    visited = [[0] * m for _ in range(n)]
    visited[start[i][0]][start[i][1]] = 1

    while q:
        x, y = q.popleft()
        for dxy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            dx = x + dxy[0]
            dy = y + dxy[1]
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            if board[dx][dy] == 'W':
                continue
            if visited[dx][dy] != 0:
                continue
            q.append((dx, dy))
            visited[dx][dy] = visited[x][y] + 1
    
    for arr in visited:
        ans = max(ans, max(arr) - 1)

print(ans)