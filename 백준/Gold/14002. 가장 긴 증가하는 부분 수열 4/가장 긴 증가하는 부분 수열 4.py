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

mx = -1
idx = 0
for i in range(n):
    if mx < dp[i]:
        mx = dp[i]
        idx = i
print(mx)

ans = []
while idx != -1:
    ans.append(arr[idx])
    idx = prev[idx]
print(*ans[::-1])