import sys
input = sys.stdin.readline 
from collections import deque
sys.setrecursionlimit(10 ** 5)

def path_print(x):
    ans = []
    tmp = x
    for _ in range(dist[k] + 1):
        ans.append(tmp)
        tmp = path[tmp]
    ans.reverse()
    print(*ans)


n, k = map(int, input().split())

visited = [False] * 100010
q = deque()
q.append(n)
visited[n] = True

dist = [0] * 100010
path = [0] * 100010
while q:
    cur = q.popleft()
    if cur == k:
        print(dist[k])
        path_print(k)
        break
    for nxt in [cur + 1, cur - 1, cur * 2]:
        if nxt < 0 or nxt >= 100010:
            continue
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1
        path[nxt] = cur