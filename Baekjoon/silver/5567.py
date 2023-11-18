from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
q = deque()
q.append((1, 0))
visited[1] = True

ans = 0

while q:
    cur, cnt = q.popleft()
    if cnt == 2:
        break
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        q.append((nxt, cnt + 1))
        visited[nxt] = True
        ans += 1

print(ans)