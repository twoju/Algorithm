import sys
input = sys.stdin.readline

n = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(n)]

def recur(cur, prev):
    if cur == n:
        return 0
    if dp[cur][prev] != -1:
        return dp[cur][prev]
    ret = 10000000
    for i in range(3):
        if prev == i:
            continue
        ret = min(ret, recur(cur + 1, i) + cost[cur][i])
    dp[cur][prev] = ret
    return dp[cur][prev]

dp = [[-1] * 3 for _ in range(n)]
print(recur(0, -1))