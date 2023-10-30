import sys
input = sys.stdin.readline


n = int(input())
dp = [[0] * n for _ in range(n)]
numbers = list(map(int, input().split()))

for i in range(n):
    for start in range(n - i):
        end = start + i
        if i == 0:
            dp[start][end] = 1
            continue
        if i == 1:
            if numbers[start] == numbers[end]:
                dp[start][end] = 1
                continue
        if numbers[start] == numbers[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])