n = int(input())
point = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = point[0]

if n == 1:
    print(dp[0])
elif n == 2:
    print(dp[0] + point[1])
else:
    dp[1] = dp[0] + point[1] 
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + point[i - 1], dp[i - 2]) + point[i]
    print(dp[n - 1])