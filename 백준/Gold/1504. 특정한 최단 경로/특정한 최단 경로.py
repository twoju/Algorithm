import sys
input = sys.stdin.readline
import heapq

def dijk(x, d):
    q = []
    heapq.heappush(q, (x, 0))
    d[x] = 0
    while q:
        x, dist_x = heapq.heappop(q)
        if dist_x != d[x]:
            continue
        for u, weight in graph[x]:
            if d[u] > d[x] + weight:
                d[u] = d[x] + weight
                heapq.heappush(q, (u, d[u]))

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v, w = map(int, input().split())

dist_v = [1e9] * (n + 1)
dist_w = [1e9] * (n + 1)


dijk(v, dist_v)
dijk(w, dist_w)

type_v = dist_v[1] + dist_v[w] + dist_w[n]
type_w = dist_w[1] + dist_w[v] + dist_v[n]

ans = min(type_v, type_w)
if ans >= 1e9:
    print(-1)
else:
    print(ans)