first = list(input())
second = list(input())
f, s = len(first) + 1, len(second) + 1
dp = [[0] * s for _ in range(f)]

for i in range(1, f):
    for j in range(1, s):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[f - 1][s - 1])