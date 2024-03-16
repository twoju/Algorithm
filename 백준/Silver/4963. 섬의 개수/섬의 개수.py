import sys
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        dx, dy = x + dxy[i][0], y + dxy[i][1]
        if dx < 0 or dy < 0 or dx >= h or dy >= w:
            continue
        if visited[dx][dy]:
            continue
        if board[dx][dy] == 1:
            dfs(dx, dy)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    ans = 0
    dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(h):
        for y in range(w):
            if board[x][y] == 1 and not visited[x][y]:
                dfs(x, y)
                ans += 1

    print(ans)