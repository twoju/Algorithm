import sys
input = sys.stdin.readline
from collections import deque

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[b] = parent[a]


n, k = map(int, input().split())
parent = [i for i in range(k + 1)]
visited = [[0 for _ in range(2001)] for _ in range(2001)]
dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)]

q = deque()
for i in range(1, k + 1):
    x, y = map(int, input().split())
    q.append((x, y, i, 0))


def bfs():
    cnt = 0
    while q:
        x, y, c, t = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = c
        for i in range(4):
            dx, dy = x + dxy[i][0], y + dxy[i][1]
            if dx < 1 or dy < 1 or dx > n or dy > n:
                continue
            cur = visited[dx][dy]
            if cur:
                if find(c) != find(cur):
                    union(c, parent[cur])
                    cnt += 1
                    if cnt == k - 1:
                        return t
                else:
                    q.append((dx, dy, c, t + 1))

print(bfs())