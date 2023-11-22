import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100010
q = deque()
q.append(n)
visited[n] = 0
cnt = 0

while q:
    cur = q.popleft()
    if cur == k:
        cnt += 1
        continue
    for nxt in [cur + 1, cur -1, cur * 2]:
        if nxt < 0 or nxt >= 100010:
            continue
        if visited[nxt] == -1 or visited[nxt] >= visited[cur] + 1:
            q.append(nxt)
            visited[nxt] = visited[cur] + 1


print(visited[k])
print(cnt)