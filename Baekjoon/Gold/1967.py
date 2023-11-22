import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    root, child, w = map(int, input().split())
    graph[root - 1].append((child - 1, w))
    graph[child - 1].append((root - 1, w))

# 처음에는 depth 를 해야한다. depth 에 가중치 더해서
def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt[0] == prev:
            continue
        if weight[nxt[0]] == 0:
            weight[nxt[0]] = weight[cur] + nxt[1]
            dfs(nxt[0], cur)

def find_dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt[0] == prev:
            continue
        find_dfs(nxt[0], cur)
        if ans[cur] != 0:
            ans[cur] = max(ans[cur], ans[nxt[0]] + nxt[1])
        else:
            ans[cur] += ans[nxt[0]] + nxt[1]


weight = [0 for _ in range(n)]
dfs(0, 0)

idx = weight.index(max(weight))
ans = [0 for _ in range(n)]
find_dfs(idx, idx)

print(max(ans))
