import sys
input = sys.stdin.readline

def dfs(cur):
    global cnt, ans
    cnt += 1
    visited[cur] = True
    if cur == b:
        ans = max(ans, cnt)
    for nxt in family[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)
    cnt -= 1

n = int(input().strip())
a, b = map(int, input().split())

family = [[] for _ in range(n + 1)]

m = int(input().strip())
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False] * (n + 1)
cnt = 0
ans = 0
dfs(a)
if ans == 0:
    print(-1)
else:
    print(ans - 1)