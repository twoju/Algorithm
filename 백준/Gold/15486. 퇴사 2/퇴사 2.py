import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def recur(cur):
    if cur > n:
        return -10000000
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return dp[cur]


n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * 1500010
print(recur(0))