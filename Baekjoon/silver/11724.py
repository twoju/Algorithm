import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True
    for i in graph[cur]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            ans += 1
            visited[i] = True
        else:
            dfs(i)
            ans += 1

print(ans)

