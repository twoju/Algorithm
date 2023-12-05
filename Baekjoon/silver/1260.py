import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

selected = [False] * (n + 1)
selected[start] = True
ans = []

def dfs(cur):
    ans.append(cur)
    for nxt in sorted(graph[cur]):
        if selected[nxt]:
            continue
        selected[nxt] = True
        dfs(nxt)


dfs(start)
print(*ans)

q = deque()
q.append(start)

visited = [False] * (n + 1)
bfs = [start]
visited[start] = True
while q:
    cur = q.popleft()
    for nxt in sorted(graph[cur]):
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True
        bfs.append(nxt)

print(*bfs)