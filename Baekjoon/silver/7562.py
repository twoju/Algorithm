import sys
from collections import deque
input = sys.stdin.readline

dxy = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        cx, cy = q.popleft()
        if cx == end_x and cy == end_y:
            print(dist[end_x][end_y])
            break
        for nxt in dxy:
            x, y = cx + nxt[0], cy + nxt[1]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if visited[x][y]:
                continue
            q.append((x, y))
            visited[x][y] = True
            dist[x][y] = dist[cx][cy] + 1
            