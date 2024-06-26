import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        ans[nxt] = cur
        dfs(nxt, cur)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (n + 1)
dfs(1, 1)
for i in range(2, n + 1):
    print(ans[i])