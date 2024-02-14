import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [-1] * (n + 2)
dp[0] = 1
dp[1] = 2

for cur in range(2, n):
    dp[cur] = (dp[cur - 1] + dp[cur - 2]) % 10007

print(dp[n - 1])