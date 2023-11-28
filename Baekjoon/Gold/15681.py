import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        # cur을 루트로하는 서브트리의 정점의 수 카운트
        dfs(nxt, cur)
        score[cur] += score[nxt]

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


score = [1] * (n + 1)
dfs(r, r)

for _ in range(q):
    point = int(input())
    print(score[point])