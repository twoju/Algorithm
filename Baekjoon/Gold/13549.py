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
    if cur * 2 < 100010 and visited[cur * 2] == False:
        q.appendleft(cur * 2)
        visited[cur * 2] = True
        dist[cur * 2] = dist[cur]
    for nxt in [cur - 1, cur + 1]:
        if nxt < 0 or nxt >= 100010:
            continue
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1