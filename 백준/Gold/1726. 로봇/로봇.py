import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
roots = [list(map(int, input().split())) for _ in range(m)]
sr, sc, di = map(int, input().split())
er, ec, ed = map(int, input().split())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
change = [(3, 4), (3, 4), (1, 2), (1, 2)]

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1))

def bfs():
    visited = [[[0] * 4 for _ in range(n)] for _ in range(m)]
    visited[sr-1][sc-1][di-1] = 1
    Q = deque([(sr-1, sc-1, di-1, 0)])
    while Q:
        r, c, d, cnt = Q.popleft()
        if (r, c, d) == (er-1, ec-1, ed-1):
            return cnt

        for dis in range(1, 4):
            nr = r + dr[d] * dis
            nc = c + dc[d] * dis
            nd = d

            if not (0 <= nr < m and 0 <= nc < n) or roots[nr][nc]:
                break
            if visited[nr][nc][nd]:
                continue
            Q.append((nr, nc, nd, cnt+1))
            visited[nr][nc][nd] = 1

        for nd in change_dir[d]:
            if visited[r][c][nd]:
                continue
            Q.append((r, c, nd, cnt+1))
            visited[r][c][nd] = 1

print(bfs())