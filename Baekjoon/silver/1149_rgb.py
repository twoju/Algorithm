def recur(cur, prev):
    if cur == n:
        return 0
    min_cost = 1000000
    if dp[cur][prev] != -1:
        return dp[cur][prev]
    for i in range(3):
        if i == prev:
            continue
        min_cost = min(recur(cur + 1, i) + cost[cur][i], min_cost)
    dp[cur][prev] = min_cost
    return dp[cur][prev]

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * 3 for _ in range(n)]
print(recur(0, -1))