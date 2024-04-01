import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
counts = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    counts[b] += 1

q = deque()

for i in range(1, n + 1):
    if not counts[i]:
        q.append(i)

ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for nxt in graph[cur]:
        counts[nxt] -= 1
        if counts[nxt]:
            continue
        q.append(nxt)

print(*ans)