import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().split()))
m = int(input().strip())
brr = list(map(int, input().split()))

sub_a = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        res = sum(arr[i:j + 1])
        sub_a[res] += 1

ans = 0
for i in range(m):
    for j in range(i, m):
        res = t - sum(brr[i:j + 1])
        ans += sub_a[res]

print(ans)