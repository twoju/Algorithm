import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(cur):
    visited[cur] = True
    arr.append(A[cur - 1])
    for i in friend[cur]:
        if visited[i]:
            continue
        dfs(i)


n, m, k = map(int, input().split())
A = list(map(int, input().split()))

friend = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    v, w = map(int, input().split())
    friend[v].append(w)
    friend[w].append(v)

ans = 0
for i in range(1, n + 1):
    arr = []
    if not visited[i]:
        dfs(i)
        ans += min(arr)

if all(visited[1:]):
    if ans <= k:
        print(ans)
    else:
        print('Oh no')
else:
    print('Oh no')