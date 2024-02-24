import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
for h in range(1, 31):
    dp[h][0] = 1

for w in range(1, 31):
    for h in range(30):
        if h == 0:
            dp[h][w] = dp[h + 1][w - 1]
        else:
            dp[h][w] = dp[h + 1][w - 1] + dp[h - 1][w]

while True:
    n = int(input().strip())
    if n == 0:
        break
    print(dp[0][n])