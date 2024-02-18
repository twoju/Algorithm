import sys
input = sys.stdin.readline

def recur(cur, w):
    if w > k:
        return -123123123
    if cur == n:
        return 0
    if dp[cur][w] != -1:
        return dp[cur][w]
    dp[cur][w] = max(recur(cur + 1, w + stuffs[cur][0]) + stuffs[cur][1], recur(cur + 1, w))
    return dp[cur][w]

n, k = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * 100010 for _ in range(n)]
print(recur(0, 0))