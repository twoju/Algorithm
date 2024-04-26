import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())

lifeguards = []
d = defaultdict(int)
for _ in range(n):
    s, e = map(int, input().split())
    lifeguards.append((s, e))
    for i in range(s, e):
        d[i] += 1

ans = 0
for i in range(n):
    s, e = lifeguards[i]
    cnt = len(d)
    for j in range(s, e):
        if d[j] == 1:
            cnt -= 1
    ans = max(ans, cnt)

print(ans)
