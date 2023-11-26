import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur):
    for nxt in graph[cur]:
        score[nxt] += score[cur]
        dfs(nxt)

n, m = map(int, input().split())

arr = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

score = [0] * (n + 1)

for i in range(1, n):
    graph[arr[i]].append(i + 1)

for _ in range(m):
    a, b = map(int, input().split())
    score[a] += b

dfs(1)
print(*score[1:])