import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())
d = defaultdict(int)
for _ in range(n):
    book = str(input().strip())
    d[book] += 1

ans = []
maxnum = max(d.values())
for i in d.keys():
    if d[i] == maxnum:
        ans.append(i)
ans.sort()
print(ans[0])