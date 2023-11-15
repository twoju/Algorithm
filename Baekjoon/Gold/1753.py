import heapq
import sys
input = sys.stdin.readline

def check(cur):
    q = []
    heapq.heappush(q, (0, cur))
    dist[cur] = 0
    while q:
        x, n = heapq.heappop(q)
        if dist[n] < x:
            continue
        for i, j in graph[n]:
            if dist[i] > x + j:
                dist[i] = x + j
                heapq.heappush(q, (x + j, i))


v, e = map(int, input().split())

k = int(input())
graph = [[] for _ in range(v + 1)]
dist = [int(1e9)] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

check(k)

for i in range(1, v + 1):
    if dist[i] == int(1e9):
        print('INF')
    else:
        print(dist[i])