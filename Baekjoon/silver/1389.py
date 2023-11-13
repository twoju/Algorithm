import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
ans = [0] * (n + 1)
ans[0] = 500000
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    q.append(i)
    visited[i] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1

    ans[i] = sum(dist)

print(ans.index(min(ans)))
            
