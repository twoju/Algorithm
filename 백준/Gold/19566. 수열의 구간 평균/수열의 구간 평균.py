import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))

pref_sum = [0] * (n + 1)
for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + A[i - 1]

ans = 0
d = defaultdict(int)
for i in range(1, n + 1):
    summ = pref_sum[i] - k * i
    ans += d[summ]
    d[summ] += 1    

print(ans + d[0])