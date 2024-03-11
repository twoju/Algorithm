def dfs(x, y):
    global home
    home += 1
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == 0:
            continue
        dfs(nx, ny)
    return home


n = int(input())
board = [list(map(int, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
cnt = 0
ans = []
home = 0

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            cnt += 1
            ans.append(dfs(i, j))
            home = 0
print(cnt)
ans.sort()
for i in ans:
    print(i)
