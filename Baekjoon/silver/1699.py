# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# def recur(cur):
#     if cur == n:
#         return 0
#     if dp[cur] != -1:
#         return dp[cur]
#     ans = 100000
#     for i in range(1, int(n ** 0.5) + 1):
#         if i ** 2 > n - cur:
#             break
#         ans = min(ans, recur(cur + (i ** 2)) + 1)
#     dp[cur] = ans
#     return dp[cur]
    

# n = int(input())
# dp = [-1] * 100001
# print(recur(0))


n = int(input())
dp = [100000] * 100001
dp[0] = 0
for cur in range(1, n + 1):
    for i in range(1, int(n ** 0.5) + 1):
        dp[cur] = min(dp[cur], dp[cur - i**2] + 1)

print(dp[n])