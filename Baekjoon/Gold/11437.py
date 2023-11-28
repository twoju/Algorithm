def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        dfs(nxt, cur)
        ans[cur] += 1

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

m = int(input())

for _ in range(m):
    left, right = map(int, input().split())
    ans = [0 for _ in range(n + 1)]
    dfs(left, left)