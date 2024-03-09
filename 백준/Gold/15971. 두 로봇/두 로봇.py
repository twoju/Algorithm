import sys
input = sys.stdin.readline
from collections import deque

n, f, s = map(int, input().split())
crave = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, l = map(int, input().split())
    crave[u].append((v, l))
    crave[v].append((u, l))

visited = [False] * (n + 1)
q = deque([(f, 0, 0)])
while q:
    cur, total, tmp = q.pop()
    visited[cur] = True
    if cur == s:
        print(total - tmp)
        exit(0)
    for nxt, cnt in crave[cur]:
        if visited[nxt]:
            continue
        q.appendleft((nxt, total + cnt, max(tmp, cnt)))
