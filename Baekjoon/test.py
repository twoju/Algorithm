import sys
input = sys.stdin.readline

def dfs(r, c):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if visited[nr][nc]:
            continue
        if cabage[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)



t = int(input().strip())
for _ in range(t):
    m, n, k = map(int, input().split())
    cabage = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        cabage[x][y] = 1
    visited = [[0] * m for _ in range(n)]
    ans = 0

    for r in range(n):
        for c in range(m):
            if cabage[r][c] and not visited[r][c]:
                visited[r][c] = True
                dfs(r, c)
                ans += 1

    print(ans)