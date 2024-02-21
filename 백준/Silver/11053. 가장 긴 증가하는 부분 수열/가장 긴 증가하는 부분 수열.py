import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
prev = [-1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

print(max(dp))