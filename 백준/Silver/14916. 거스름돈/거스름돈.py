import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def recur(cur):
    if cur > n:
        return 10000000
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = min(recur(cur + 2) + 1, recur(cur + 5) + 1)
    return dp[cur]

n = int(input().strip())
dp = [-1] * 100001
ans = recur(0)
if ans == 10000001:
    print(-1)
else:
    print(ans)