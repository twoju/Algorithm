import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur):
    for i in graph[cur]:
        if visited[i] == 0:
            visited[i] = cur
            dfs(i)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

dfs(1)

for i in range(2, n + 1):
    print(visited[i])