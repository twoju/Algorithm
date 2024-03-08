import sys
input = sys.stdin.readline

def dfs(cur):
    cnt = 1
    visited[cur] = True
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        cnt += dfs(nxt)
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if len(graph[i]) == 0:
        cnt += 1
    else:
        if dfs(i) - 1:
            cnt += 1
print(cnt)