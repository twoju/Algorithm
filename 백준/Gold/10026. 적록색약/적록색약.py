import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, cur):
    visited[x][y] = True
    for nxt in range(4):
        dx = x + dxy[nxt][0]
        dy = y + dxy[nxt][1]
        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            continue
        if visited[dx][dy]:
            continue
        if original[dx][dy] == cur:
            dfs(dx, dy, cur)

n = int(input().strip())
original = []
rgb = []
for _ in range(n):
    arr = input().strip()
    original.append(arr)
    change = ''
    for i in range(n):
        if arr[i] == 'G':
            change += 'R'
        else:
            change += arr[i]
    rgb.append(change)

ans = [0, 0]
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

visited = [[False] * n for _ in range(n)]
for cur in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if original[i][j] == cur:
                dfs(i, j, cur)
                ans[0] += 1

original = rgb
visited = [[False] * n for _ in range(n)]
for cur in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if original[i][j] == cur:
                dfs(i, j, cur)
                ans[1] += 1

print(*ans)