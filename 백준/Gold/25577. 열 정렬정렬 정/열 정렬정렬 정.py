import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input().strip())
arr = list(map(int, input().split()))

todo = sorted(arr[:])
d = defaultdict(int)
deg = defaultdict(int)
for i in range(n):
    d[arr[i]] = todo[i]
    deg[arr[i]] += 1
    if arr[i] != todo[i]:
        deg[todo[i]] += 1

q = deque()
visited = defaultdict(int)
ans = 0
for i in arr:
    if visited[i]:
        continue
    if deg[i] == 1:
        continue
    q.append(i)
    while q:
        cur = q.popleft()
        if visited[d[cur]]:
            continue
        ans += 1
        visited[cur] = 1
        q.append(d[cur])

print(ans)