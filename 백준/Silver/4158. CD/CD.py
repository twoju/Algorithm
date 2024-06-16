import sys
input = sys.stdin.readline
from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    d = defaultdict(int)
    for _ in range(n + m):
        a = int(input().strip())
        d[a] += 1
    cnt = 0
    for i in d.values():
        if i > 1:
            cnt += 1
    print(cnt)