import sys
import heapq
input = sys.stdin.readline

n, m, end = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dik(x):
    q = []
    dist = [1e9] * (n + 1)

    heapq.heappush(q, (0, x))
    dist[x] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist[x] < dist_x:
            continue
        for u, w in graph[x]:
            if dist[u] > dist_x + w:
                dist[u] = dist_x + w
                heapq.heappush(q, (dist[u], u))
    return dist

ans = dik(end)
ans[0] = 0

for i in range(1, n + 1):
    if i != end:
        res = dik(i)
        ans[i] += res[end]

print(max(ans))