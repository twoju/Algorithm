import sys
input = sys.stdin.readline
from collections import deque
    

n, k = map(int, input().split())
visited = [False] * 100010
dist = [0] * 100010
q = deque()
q.append(n)
visited[n] = True

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[k])
        break
    if cur * 2 <= 100000 and visited[cur * 2] == False:
        q.appendleft(cur * 2)
        dist[cur * 2] = dist[cur]
        visited[cur * 2] = True
    for nxt in [cur - 1, cur + 1]:
        if nxt < 0 or nxt >= 100010:
            continue
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1