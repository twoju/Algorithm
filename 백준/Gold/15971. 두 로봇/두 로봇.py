import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(cur, total, cnt):
    visited[cur] = True
    if cur == s:
        print(total - cnt)
        exit(0)
    for nxt, w in crave[cur]:
        if visited[nxt]:
            continue
        dfs(nxt, total + w, max(w, cnt))


n, f, s = map(int, input().split())
crave = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, l = map(int, input().split())
    crave[u].append((v, l))
    crave[v].append((u, l))

visited = [False] * (n + 1)
ans = 1e9
if f == s:
    print(0)
else:
    dfs(f, 0, 0)