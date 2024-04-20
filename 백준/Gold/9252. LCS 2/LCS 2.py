import sys
input = sys.stdin.readline

a = [''] + list(input().strip())
b = [''] + list(input().strip())

len_a = len(a)
len_b = len(b)

dp = [[0] * len_b for _ in range(len_a)]

for i in range(1, len_a):
    for j in range(1, len_b):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

n = dp[len_a - 1][len_b - 1]
print(n)

lcs = ''
s, e = len_a - 1, len_b - 1
while s > 0 and e > 0:
    if a[s] == b[e]:
        lcs = a[s] + lcs
        if len(lcs) == n:
            print(lcs)
            break
        s -= 1
        e -= 1
    else:
        if dp[s - 1][e] > dp[s][e - 1]:
            s -= 1
        else:
            e -= 1