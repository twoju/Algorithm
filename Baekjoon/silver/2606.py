def dfs(cur):
    cnt = 1
    visited[cur] = True
    for i in network[cur]:
        if visited[i]:
            continue
        cnt += dfs(i)
    return cnt


n = int(input())
m = int(input())

network = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

print(dfs(1) - 1)