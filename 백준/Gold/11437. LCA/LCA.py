import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        ans[nxt] = cur
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] < depth[b]:
            b = ans[b]
        else:
            a = ans[a]
    while a != b:
        a = ans[a]
        b = ans[b]
    return a

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

m = int(input())

ans = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

dfs(1, 0)

for _ in range(m):
    left, right = map(int, input().split())

    print(lca(left, right))