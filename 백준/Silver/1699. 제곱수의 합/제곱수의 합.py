n = int(input())
dp = [100000] * 100001
dp[0] = 0
for cur in range(1, n + 1):
    for i in range(1, int(n ** 0.5) + 1):
        dp[cur] = min(dp[cur], dp[cur - i**2] + 1)

print(dp[n])