import sys
input = sys.stdin.readline

ans = 0
x, y = 0, 0
for i in range(1, 10):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] >= ans:
            ans = arr[j]
            x, y = i, j + 1

print(ans)
print(x, y)

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