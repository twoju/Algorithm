import sys
input = sys.stdin.readline

n = int(input().strip())
time = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
ret = -1500000000
for cur in range(n):
    ret = max(ret, dp[cur])
    if cur + time[cur][0] > n:
        continue
    dp[cur + time[cur][0]] = max(ret + time[cur][1], dp[cur + time[cur][0]])

print(max(dp))