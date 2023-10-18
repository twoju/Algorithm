# def recur(cur):
#     if cur > n:
#         return -123123123
#     if cur == n:
#         return 0
#     if dp[cur] != -1:
#         return dp[cur]
#     dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
#     return dp[cur]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n + 1)
# print(recur(0))

cost = -12312123123
for cur in range(n):
    cost = max(cost, dp[cur])
    if cur + arr[cur][0] > n:
        continue
    dp[cur + arr[cur][0]] = max(cost + arr[cur][1], dp[cur + arr[cur][0]])

print(max(dp) + 1)