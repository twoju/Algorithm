def dfs(cur):
    visited[cur] = True
    if first == second:
        ans.extend(sorted(first))
        return
    for i in number[cur]:
        if not visited[i]:
            first.append(cur)
            second.append(i)
            print(first, second)
            dfs(i)


n = int(input())

number = [[] for _ in range(0, n + 1)]

for i in range(n):
    a = int(input())
    number[a].append(i + 1)

print(number)

ans = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    first = []
    second = []
    if not visited[i]:
        dfs(i)

print(len(ans))
for i in ans:
    print(i)