import sys
input = sys.stdin.readline

def dfs(cur):
    cnt = 1
    visited[cur] = True
    for nxt in computers[cur]:
        if visited[nxt]:
            continue
        cnt += dfs(nxt)
    return cnt

n = int(input().strip())
m = int(input().strip())

computers = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    computers[u].append(v)
    computers[v].append(u)

visited = [False] * (n + 1)
print(dfs(1) - 1)