import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [False] * 100010
dist = [0] * 100010

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[k])
        break
    for nxt in [cur - 1, cur + 1, 2 * cur]:
        if nxt < 0 or nxt >= 100010:
            continue
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1