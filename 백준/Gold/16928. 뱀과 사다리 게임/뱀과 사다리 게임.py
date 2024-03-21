import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
ladder = [0] * 101

for _ in range(n + m):
    x, y = map(int, input().split())
    ladder[x] = y

q = deque()
q.append((1, 0))
visited = [False] * 101
ans = 1e9
visited[1] = True
while q:
    cur, cnt = q.popleft()
    if cur == 100:
        ans = min(ans, cnt)
        break
    for i in range(1, 7):
        if cur + i > 100:
            continue
        if visited[cur + i]:
            continue
        if ladder[cur + i] != 0:
            q.append((ladder[cur + i], cnt + 1))
        else:
            q.append((cur + i, cnt + 1))
        visited[cur] = True

print(ans)