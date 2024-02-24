import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n - 1)]
dp[0][nums[0]] = 1
for cur in range(1, n - 1):
    for res in range(21):
        if res + nums[cur] <= 20:
            dp[cur][res + nums[cur]] += dp[cur - 1][res]
        if res - nums[cur] >= 0:
            dp[cur][res - nums[cur]] += dp[cur - 1][res]

print(dp[n - 2][nums[-1]])