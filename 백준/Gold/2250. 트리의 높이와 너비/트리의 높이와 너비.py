import sys
input = sys.stdin.readline
from collections import defaultdict


def dfs(cur):
    global max_depth
    for nxt in graph[cur]:
        if nxt == -1:
            continue
        depth[nxt] = depth[cur] + 1
        max_depth = max(max_depth, depth[nxt])
        dfs(nxt)

def inorder(cur):
    global col_num
    if graph[cur][0] != -1:
        inorder(graph[cur][0])
    col[depth[cur]].append(col_num)
    col_num += 1
    if graph[cur][1] != -1:
        inorder(graph[cur][1])

n = int(input().strip())
graph = [[0] * 2 for _ in range(10001)]

d = defaultdict(int)
for _ in range(n):
    node, l, r = map(int, input().split())
    for i in [node, l, r]:
        if i == -1:
            continue
        d[i] += 1
    graph[node][0], graph[node][1] = l, r

start = min(d, key=d.get)
depth = [0] * (n + 1)
max_depth = 0
dfs(start)

col = [[] * (n + 1) for _ in range(max_depth + 1)]

col_num = 1
inorder(start)

ans = [1, 1]
for i in range(max_depth + 1):
    if len(col[i]) == 1:
        calc = 1
    else:
        calc = max(col[i]) - min(col[i]) + 1
    if calc > ans[1]:
        ans = [i + 1, calc]

print(*ans)