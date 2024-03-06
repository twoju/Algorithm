import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[board[nx][ny]] == 1:
            continue
        visited[board[nx][ny]] += 1
        dfs(nx, ny, cnt + 1)
        visited[board[nx][ny]] -= 1


r, c = map(int, input().split())

board = []
for _ in range(r):
    alpha = list(map(lambda a: ord(a)-65,input().strip()))
    board.append(alpha)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ans = 1
visited = [0] * 26
visited[board[0][0]] = 1
dfs(0, 0, 1)
print(ans)