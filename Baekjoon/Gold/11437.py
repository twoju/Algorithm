import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cur, dep):
    visited[cur] = True
    depth[cur] = dep
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        ans[nxt] = cur
        dfs(nxt, dep + 1)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = ans[a]
        else:
            b = ans[b]
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
visited = [False for _ in range(n + 1)]

dfs(1, 0)

for _ in range(m):
    left, right = map(int, input().split())
    print(lca(left, right))
    
    # while True:
    #     if depth[left] == depth[right]:
    #         break
    #     if depth[left] > depth[right]:
    #         left = ans[left]
    #     else:
    #         right = ans[right]

    # while True:
    #     if left == right:
    #         break
    #     left = ans[left]
    #     right = ans[right]

    # print(left)