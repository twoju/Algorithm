import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == c - 1:
        return True
    for nxt in [-1, 0, 1]:
        nx, ny = x + nxt, y + 1
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == 1:
            continue
        visited[nx][ny] = True
        if dfs(nx, ny):
            return True
    return False


r, c = map(int, input().split())
board = []
for _ in range(r):
    arr = list(map(lambda x: 0 if x == '.' else 1, input().strip()))
    board.append(arr)
ans = 0
visited = [[False] * c for _ in range(r)]
for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)

# -----
# // recur(인자, 인자) => 인자만큼 dp를 만들면 된다
# dp[l][r][bld]
# def recur(cur, l, r):
    #     if l > r:
    #  return 0
#     if cur == 3 * n:
#         return 0
#     if dp[l][r] != -1:
#         return dp[l][r]
#     if turn[cur % 3] == state[l]:
#         recur(cur + 1, l + 1, r)
#     if turn[cur % 3] == state[r]:
#         recur(cur + 1, l, r - 1)
#     return dp[l][r]


# n = int(input().strip())
# state = list(map(str, input().strip()))

# turn = 'BLD'
# dp = [[-1] * (3 * n) for _ in range(3 * n)]
# print(recur(0, 0, 3 * n - 1))