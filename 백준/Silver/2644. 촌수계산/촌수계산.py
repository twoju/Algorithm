def dfs(cur):
    global cnt
    cnt += 1
    visited[cur] = True
    if cur == s:
        ans.append(cnt)
    for nxt in family[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)
    cnt -= 1
    


n = int(input())
f, s = map(int, input().split())

family = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
ans = []

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

dfs(f)

if len(ans) == 0:
    print(-1)
else:
    print(ans[0] - 1)