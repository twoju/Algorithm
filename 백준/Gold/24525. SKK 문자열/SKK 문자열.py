import sys
input = sys.stdin.readline
from collections import defaultdict

arr = list(map(str, input().strip()))
n = len(arr)
prefix = [0] * (n + 1)
cnt = [0] * (n + 1)

for i in range(n):
    if arr[i] == 'S':
        prefix[i + 1] += 2
        cnt[i + 1] += 1
    if arr[i] == 'K':
        prefix[i + 1] -= 1
        cnt[i + 1] += 1
    prefix[i + 1] += prefix[i]
    cnt[i + 1] += cnt[i]

ans = -1
d = defaultdict(int)
for i in range(n + 1):
    if prefix[i] not in d:
        d[prefix[i]] = i
    else:
        idx = d[prefix[i]]
        if cnt[idx] == cnt[i]:
            continue
        ans = max(ans, i - idx)

print(ans)