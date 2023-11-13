import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s].append([e, c])

start, end = map(int, input().split())
dist = [1e9] * (n + 1)

q = []
dist[start] = 0
heapq.heappush(q, [start, 0])

while q:
    cur, cost = heapq.heappop(q)
    if dist[cur] < cost:
        continue
    for nxt, nxt_c in bus[cur]:
        sum_c = cost + nxt_c
        if sum_c >= dist[nxt]:
            continue
        dist[nxt] = sum_c
        heapq.heappush(q, [nxt, sum_c])

print(dist[end])

# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# bus = [[] for _ in range(n + 1)]
# cost = [[0] * (n + 1) for _ in range(m + 1)]
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     bus[s].append(e)
#     cost[s][e] = c

# start, end = map(int, input().split())
# dist = [100010] * (n + 1)

# q = deque()
# q.append(start)
# dist[start] = 0

# while q:
#     cur = q.popleft()
#     if cur == end:
#         print(dist[end])
#         break
#     for nxt in bus[cur]:
#         q.append(nxt)
#         dist[nxt] = min(dist[cur] + cost[cur][nxt], dist[nxt])